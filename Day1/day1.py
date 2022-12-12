
file = open('elves.txt', 'r')
lines = file.readlines()
print("lines read",len(lines))

numElves = 0
loadCurrentElf = 0
maxLoad = 0
loads = []

for line in lines:
    line = line.strip()
    if line.isnumeric():
        loadCurrentElf += int(line)
    else: #Change of elf
        if loadCurrentElf > maxLoad:
            maxLoad = loadCurrentElf
        loads.append(loadCurrentElf)
        numElves+= 1
        loadCurrentElf = 0


print("Total elves", numElves)
print("Max Load", maxLoad)
maxLoads = sorted(loads, reverse=True)[:3]
print("Max Load", maxLoads)

print("Max 3 Loads", sum(maxLoads))
