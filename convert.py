import sys

if len(sys.argv) < 2:
    print("Please specify a file to modify")
    sys.exit(0)

f = open(sys.argv[1], 'r')
lines = f.readlines()

for line in lines:
    items = line.split(' ')
    if len(items) < 3:
        continue
    if "*" in items[-1]:
        items = items[:-1]

    printing_index=0

    # find (MOC)
    for (idx, item) in enumerate(items):
        if "(" in item:
            printing_index=idx
    
    # break off ()
    items[printing_index] = items[printing_index][1:-1]

    print(f"{items[0]} [{items[printing_index]}:{items[-1].strip()}] {' '.join(items[1:printing_index])}",)
