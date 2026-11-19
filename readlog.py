import sys

def count_keywords(lines,keywords):
    counts = {}
    for kw in keywords:
        counts[kw] = 0
    for line in lines:
        for kw in keywords:
            if kw in line:
                counts[kw] = counts[kw] + 1
    return counts


filename = sys.argv[1]
keywords = sys.argv[2:]

f = open(filename)
content = f.read()
f.close()

lines = content.splitlines()

counts = count_keywords(lines, keywords)

print("=" * 26)
print(" " + filename + "统计结果")
print("=" * 26)

for keyword in counts:
    print(keyword.ljust(8), counts[keyword])

print("-" * 26)
print("总行数", len(lines))


