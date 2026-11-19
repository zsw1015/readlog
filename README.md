# readlog

一个命令行日志关键词统计工具。读取日志文件，统计指定关键词各出现在多少行。

## 用法

```bash
python3 readlog.py <日志文件> <关键词1> <关键词2> ...
```

示例：

```bash
python3 readlog.py app.log ERROR INFO WARN
```

输出：

```
==========================
 app.log 统计结果
==========================
ERROR    4
INFO     3
WARN     2
--------------------------
总行数 9
```

## 环境

Python 3，无需安装任何第三方库。
