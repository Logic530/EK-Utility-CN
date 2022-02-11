# EK Utility CN

为潜渊症模组 EK Utility 的 __未授权__ 汉化版本。

分支 main 为原模组经过 main.py 汉化工具处理后，其余不变的内容，分支 zh-cn 为汉化版本。

汉化版本主要修改内容包括：

+ 移除了原模组中“硬编码”的所有物品名称和描述（通过 main.py 处理工具）
+ 添加了 `Text\EnglishEKUtilities.xml`, `Text\SimplifiedChineseEkUtilities.xml` 两个文本文件，其中 `Text\EnglishEKUtilities.xml` 为 main.py 处理工具生成的原版英文文本，`Text\SimplifiedChineseEkUtilities.xml` 为手工汉化完成的中文文本文件。

## 模组更新流程

推荐使用 VSCode 进行相关操作

1. 获得原模组更新后的文件
2. 删除 main 分支下的所有与模组有关的文件
3. 将原模组文件放入 main 分支下
4. 使用 `main.py` 处理工具，对原模组进行去除硬编码的处理，并生成 `translation.xml`
5. 提交所有修改，附言为“年.月.日 更新”之类的
6. 将 main 分支合并至 zh-cn 分支，将出现若干合并冲突，除 `filelist.xml` 采用 zh-cn 分支的版本外，其余冲突均采用 main 分支的版本
   1. 将 zh-cn 分支的 `filelist.xml` 中的游戏支持版本设置为原模组一致
   2. 注意 main 分支 `filelist.xml` 中是否新增条目，如果有，也在 zh-cn 分支添加
7. 使用正则表达式 `Mods[/\\]EK Utilities[/\\]` 搜索 zh-cn 分支下的所有文件，并全部替换为 `Mods/EK Utility CN/` 
   1. 注意作者有可能~~莫名其妙~~引用自家隔壁模组的文件，如出现 `Mods/EK Armory/` 等路径，保险起见，对这些路径进行搜索，如果存在，检查本模组是否已经包含所需的文件，并相应的修改路径
8. 此时所有合并冲突应该已经全部解决，提交所有更改，完成分支合并
9. 复制 `translation.xml` 的所有内容至 zh-cn 分支下的 `Text\EnglishEKUtilities.xml` 并覆盖，VSCode 中会自动高亮有修改的部分
10. 对照以上高亮的修改部分，对 `Text\SimplifiedChineseEkUtilities.xml` 中的汉化进行相应的修改，例如修改已有的文本或添加新文本
11. 提交所有修改，附言为“更新汉化”之类的
