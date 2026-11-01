import polib
import sys

po = polib.pofile(sys.argv[1])

i = 0

for entry in po:
    if entry.obsolete or not entry.msgstr:
        continue

    if '\n' in entry.msgid and '\n' not in entry.msgstr:
        print(f"\nLine {entry.linenum}:")
        print(f"Original: {entry.msgid}")
        i = i+1
        #print(f"Translation: {entry.msgstr}")


if i > 0:
    print(f"\nTotal {i} issues in {sys.argv[1]}")

sys.exit(1 if i > 0 else 0)
