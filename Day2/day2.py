file = open('rps.txt', 'r')
lines = file.readlines()
print("lines read", len(lines))

totalScore = 0

for line in lines:
    partialScore = 0
    (opponent, me) = line.strip().split(" ")

    # First part
    # if (opponent == "A" and me == "X") or (opponent == "B" and me == "Y") or (opponent == "C" and me == "Z"):
    #     partialScore += 3 # Draw
    # elif (opponent == "A" and me == "Y") or (opponent == "B" and me == "Z") or (opponent == "C" and me == "X"):
    #     partialScore +=6 # Win
    # #else:
    # #    partialScore +=0
    
    # if me == "X":
    #     partialScore += 1
    # elif me == "Y":
    #     partialScore += 2 
    # else:   #if me == "Z":
    #     partialScore += 3

    # Second part
    if me == "Y": # Draw
        partialScore += 3
    elif me == "Z": # Win
        partialScore += 6 
    #else:   #if me == "X":
    #    partialScore += 0

    # me plays Rock
    if (opponent == "A" and me == "Y") or (opponent == "B" and me == "X") or (opponent == "C" and me == "Z"):
        partialScore += 1
    # me plays Paper 
    elif (opponent == "A" and me == "Z") or (opponent == "B" and me == "Y") or (opponent == "C" and me == "X"):
        partialScore += 2
    else:
        partialScore += 3

    totalScore += partialScore

print("total score", totalScore)