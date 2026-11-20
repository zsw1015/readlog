import sys

def count_keywords(lines,keywords):
    counts = {}
    for kw in keywords:
        counts[kw] = []
    for i, line in enumerate(lines,1):
        lower_line = line.lower()
        for kw in keywords:
            if kw.lower() in lower_line:
                counts[kw].append("L" + str(i) + ": " + line)
    return counts

if len(sys.argv) < 3:
    print("用法: python3 readlog.py <日志文件> <关键词1> ...")
    sys.exit(1)

filename = sys.argv[1]
keywords = sys.argv[2:]

f = open(filename)
content = f.read()
f.close()

lines = content.splitlines()

counts = count_keywords(lines, keywords)

report = []
report.append("=" * 26)
report.append(" " + filename + " 统计结果")
report.append("=" * 26)

for keyword in counts:
    report.append(keyword.ljust(8) + " " + str(len(counts[keyword])))
    for item in counts[keyword]:
        report.append("    " + item)

report.append("-" * 26)
report.append("总行数 " + str(len(lines)))

for r in report:
    print(r)


