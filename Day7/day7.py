from collections import defaultdict

def main():
    
    file = open('filesystem.txt', 'r')
    lines = file.readlines()
    print("lines read", len(lines))

    path = []
    dirSizes = defaultdict(int)

    for line in lines:
        line = line.strip()
        words = line.split(" ")
        
        # Command
        if words[0] == "$":
            if words[1] == "cd":
                if words[2] == '..':
                    path.pop()
                else:
                    path.append(words[2])
            #elif words[1] == 'ls':
            #   continue
    
        elif words[0] == 'dir':
            continue

        else:
            size = int(words[0])
            
            for i in range(1, len(path)+1):
                dir = "/".join(path[:i])
                dirSizes[dir] += size

    # First part
    result = 0
    for size in dirSizes.values():
        if size < 100000:
            result += size

    print("Result", result)

    # Second part
    spaceTargeted = 30000000
    spaceAvailable = 70000000 - dirSizes["/"]
    spaceNeeded = spaceTargeted - spaceAvailable


    result = 70000000
    for size in dirSizes.values():
        if size > spaceNeeded:
            if size < result:
                result = size


    print("Result", result)

if __name__ == "__main__":
    main()