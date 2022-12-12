
def splitInTwo(line):
    length = len(line)
    return line[:int(length/2)], line[int(length/2):]

def calculateScore(letter):
    letters = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letters.find(letter)

def main():
    file = open('rucksack.txt', 'r')
    lines = file.readlines()
    print("lines read",len(lines))

    score = 0

    # First part
    # for line in lines:
    #     line = line.strip()
    #     (word1, word2) = splitInTwo(line)

    #     for letter in word1:
    #         if letter in word2:
    #             break
        
    #     score += calculateScore(letter)


    for i in range(0, len(lines), 3):
        line1 = lines[i].strip()
        line2 = lines[i+1].strip()
        line3 = lines[i+2].strip()

        for letter in line1:
            if letter in line2 and letter in line3:
                break

        score += calculateScore(letter)
    
    print("Total score", score)


if __name__ == "__main__":
    main()
