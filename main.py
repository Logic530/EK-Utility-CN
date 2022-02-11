# 模组物品名称处理及汉化工具 by Logic_530
# 功能1：自动读取模组中“硬编码”的物品名称和物品描述，并整合至工作目录下 tanslation.xml 文件中。此文件即是符合游戏标准的语言文件。（语言种类为英文）
# 功能2：删除模组中“硬编码”的的物品名称及描述，使语言文件能够生效。（我不知道游戏开发者咋想的，硬编码的优先级居然比语言文件更大）

from xml.dom.minidom import parse
import xml.etree.ElementTree as ET
import re


def get_file_list(index_file):
    index_dom = parse(index_file)
    item_file_elements = index_dom.getElementsByTagName('Item')
    ls = []
    for item_file_element in item_file_elements:
        path_1 = item_file_element.attributes['file'].value
        path_2 = path_1.split('/')
        del path_2[0]
        del path_2[0]
        path = '/'.join(path_2)
        ls.append(path)
    return ls


if __name__ == '__main__':
    mod_path = input("input mod folder path")
    file_list = get_file_list(mod_path + '/filelist.xml')

    # regex pattern
    pattern_name = re.compile("<Item name=\".*?\"")
    pattern_description = re.compile("description=\".*?\"")

    trans_file = open('translation.xml', 'w')
    trans_file.write("""<?xml version="1.0" encoding="utf-8"?>\n""")
    trans_file.write("""<infotexts language="English" nowhitespace="false" translatedname="English">\n""")

    for file in file_list:
        file = mod_path + '/' + file

        i = input("parsing " + file + " (Y) to continue,N to skip,S to stop")
        if i == 'Y':
            pass
        elif i == 'N':
            continue
        elif i == 'S':
            exit()
        else:
            pass

        trans_file.write("\n<!--{}-->\n".format(file))

        file_tree = ET.parse(file)
        item_elements = file_tree.findall('Item')

        for item_element in item_elements:
            identifier = item_element.attrib['identifier']

            if "name" in item_element.attrib:
                name = item_element.attrib['name']
            else:
                name = ""
            name_element = "<entityname.{}>{}</entityname.{}>".format(identifier, name, identifier)
            # exp: <entityname.ekutility_heavytank_weldingfuel>强化焊接油罐</entityname.ekutility_heavytank_weldingfuel>
            print(name_element)
            trans_file.write(name_element + '\n')

            if "description" in item_element.attrib:
                description = item_element.attrib['description']
            else:
                description = ""
            desc_element = "<entitydescription.{}>{}</entitydescription.{}>".format(identifier, description, identifier)
            # exp: <entitydescription.ekutility_heavytank_weldingfuel>经强化的燃料罐，耐冲击和高温。</entitydescription
            # .ekutility_heavytank_weldingfuel>
            print(desc_element)
            trans_file.write(desc_element + '\n')

        i = input("do you want to remove item name and description for language file to work? (Y) N")
        if i == 'N':
            continue
        else:
            pass

        f = open(file, 'r', encoding='utf-8')
        file_string = f.read()
        f.close()

        file_string = re.sub(pattern_name, "<Item name=\"\"", file_string)
        file_string = re.sub(pattern_description, "", file_string)

        f = open(file, 'w', encoding='utf-8')
        f.write(file_string)
        f.close()

    trans_file.write("""\n\n</infotexts>""")
    trans_file.close()
    print("all done")
