import sys

def count_keywords(lines,keywords):
    counts = {}
    for kw in keywords:
        counts[kw] = []
    for i, line in enumerate(lines,1):
        for kw in keywords:
            if kw in line:
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

print("=" * 26)
print(" " + filename + " 统计结果")
print("=" * 26)

for keyword in counts:
    print(keyword.ljust(8), len(counts[keyword]))
    for item in counts[keyword]:
        print("    " + item)
print("-" * 26)
print("总行数", len(lines))


