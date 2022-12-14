

def cleanLine(line):
    line = line.strip()
    (interval1, interval2) = line.split(",")
    (start1, end1) = interval1.split("-")
    (start2, end2) = interval2.split("-")
    
    return (int(start1), int(end1), int(start2), int(end2))

def isContained(start1, end1, start2, end2):
                # int1 is bigger                        #int2 is bigger
    return (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1)

def thereIsOverlap(start1, end1, start2, end2):

    if isContained(start1, end1, start2, end2):
        return True
    
    # interval1 starts first
    if start1 < start2:
        if start2 <= end1:
            return True
    # interval2 starts first
    elif start1 > start2:
        if start1 <= end2:
            return True
    else: # both start at the same time --> There is overlap
        return True

    return False
        

def main():
    file = open('sections.txt', 'r')
    lines = file.readlines()
    print("lines read",len(lines))

    score = 0
   
    for line in lines:
        
        (start1, end1, start2, end2) = cleanLine(line)
  
        # Part 1
        #if isContained(start1, end1, start2, end2):

        # Part 2
        if thereIsOverlap(start1, end1, start2, end2):
            score += 1


    
    
    print("Total score", score)


if __name__ == "__main__":
    main()
