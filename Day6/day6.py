
def isMarker(candidate):
    # if (candidate[0] == candidate[1] or candidate[0] == candidate[2] or candidate[0] == candidate[3] or \
    #             candidate[1] == candidate[2] or candidate[1] == candidate[3] or \
    #             candidate[2] == candidate[3]):
    #             return False
    # return True

    return (candidate[0] != candidate[1] and candidate[0] != candidate[2] and candidate[0] != candidate[3] and \
                candidate[1] != candidate[2] and candidate[1] != candidate[3] and \
                candidate[2] != candidate[3])

def hasDifferentCharacters(candidate):
    
    for char in candidate:
        candidate = candidate.replace(char, "", 1)
        if candidate.find(char) != -1:
            return False

    return True

def main():
    
    file = open('markers.txt', 'r')
    lines = file.readlines()
    print("lines read", len(lines))

    for line in lines:
        #print("line", line)

        # First part
        # for index in range(len(line) - 4):
        #     candidate = line[index:index + 4]
        #     #print("candidate", candidate)
        #     if isMarker(candidate):
        #         break
        #     #if hasDifferentCharacters(candidate):
        #     #    break

        # print("Message starts at", index + 4)

        # Second part
        for index in range(len(line) - 14):
            candidate = line[index:index + 14]
            if hasDifferentCharacters(candidate):
                break

        print("Message starts at", index + 14)


if __name__ == "__main__":
    main()