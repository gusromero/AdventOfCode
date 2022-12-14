

def parseLine(line):
    line = line.strip()
    words = line.split(" ")
   
    return (int(words[1]), int(words[3]), int(words[5]))

def readStacks(lines, numStacks):
    
    stacks = []

    for i in range(numStacks+1):
        stack = []
        stacks.append(stack)
    
    lines.reverse()
    for line in lines:
        for index in range (1, numStacks+1):
            char = line[4*index - 3]
            if char != " ":
                stacks[index].append(char)

    stacks[0].append("")
    
    return stacks


def main():
    
    file = open('crates.txt', 'r')
    lines = file.readlines()
    print("lines read",len(lines))

    stacks = readStacks(lines[:8], 9)   #readStacks(lines[:3], 3)
    print(stacks)
   
    for line in lines[10:]: #lines[5:]:

        (amount, origin, destination) = parseLine(line)

        # Part 1
        #for i in range(amount):
        #    element = stacks[origin].pop()
        #    stacks[destination].append(element)

        # Part2
        elements = []
        for i in range(amount):
            elements.append(stacks[origin].pop())
        elements.reverse()
        for element in elements:
            stacks[destination].append(element)

    result = ""
    for stack in stacks:
        result += stack.pop()

    print("Result", result)

if __name__ == "__main__":
    main()
