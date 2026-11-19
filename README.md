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
    L1: ERROR disk full
    L3: ERROR timeout
    L5: ERROR connection refused
    L7: ERROR disk full
INFO     3
    L2: INFO started
    L4: INFO stopped
    L8: INFO restarted
WARN     2
    L6: WARN low memory
    L9: WARN low memory
--------------------------
总行数 9
```

## 环境

Python 3，无需安装任何第三方库。
