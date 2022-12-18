
forest = []

def isVisible(height, treesBefore):
    for tree in treesBefore:
        if tree >= height:
            return False
    return True

def isVisibleFromNorth(height, row, column):
    treesBefore = []
    rows = forest[:row]
    for row in rows:
        treesBefore.append(row[column])

    return isVisible(height, treesBefore)

def isVisibleFromSouth(height, row, column):
    treesBefore = []
    rows = forest[row+1:]
    for row in rows:
        treesBefore.append(row[column])

    return isVisible(height, treesBefore)
    
def isVisibleFromEast(height, row, column):
    treesBefore = forest[row][column+1:]
    return isVisible(height, treesBefore)    

def isVisibleFromWest(height, row, column):
    treesBefore = forest[row][:column]
    return isVisible(height, treesBefore)

def amount(height, treesBefore):
    count = 0
    for tree in treesBefore:
        count += 1
        if tree >= height:
            break
    return count

def amountFromNorth(height, row, column):
    treesBefore = []
    rows = forest[:row]
    for row in rows:
        treesBefore.append(row[column])
    treesBefore.reverse()
    return amount(height, treesBefore)

def amountFromSouth(height, row, column):
    treesBefore = []
    rows = forest[row+1:]
    for row in rows:
        treesBefore.append(row[column])

    return amount(height, treesBefore)

def amountFromEast(height, row, column):
    treesBefore = forest[row][column+1:]
    return amount(height, treesBefore)

def amountFromWest(height, row, column):
    treesBefore = forest[row][:column]
    treesBefore.reverse()
    return amount(height, treesBefore)

def main():
    
    file = open('trees.txt', 'r')
    lines = file.readlines()
    print("lines read", len(lines))

    for line in lines:
        line = line.strip()
        row = []
        for char in line:
            row.append(int(char))
        forest.append(row)

    #print(forest)
    numRows = len(forest)
    numColumns = len(forest[0])

    # # First part
    # numVisibles = 2*numRows + 2*numColumns - 4
    # print("Perimeter:", numVisibles)

    # for row in range(1, numRows-1):
    #     for column in range(1, numColumns-1):
    #         height = forest[row][column]
    #         #print("Candidate", height)
    #         if (isVisibleFromNorth(height, row, column) or isVisibleFromSouth(height, row, column) or \
    #             isVisibleFromEast(height, row, column) or isVisibleFromWest(height, row, column)):
    #             #print("Is Visible!")
    #             numVisibles += 1

    # print("Visibles:", numVisibles)

    # Second part
    maxScore = 0
    for row in range(1, numRows-1):
        for column in range(1, numColumns-1):
            height = forest[row][column]
            #print("Candidate", height)
            score = amountFromNorth(height, row, column) * amountFromSouth(height, row, column) * \
                amountFromEast(height, row, column) * amountFromWest(height, row, column)
            if score > maxScore:
                maxScore = score

    print("Score: ", maxScore)

if __name__ == "__main__":
    main()