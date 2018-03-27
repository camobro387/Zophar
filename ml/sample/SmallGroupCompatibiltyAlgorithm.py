def smallGroupScore(userMBTI, groupMBTI):
    #initialize variable for score and MBTI compatibility table
    score = 0
    compatibilityTable = [[  3,  3,  3,  4,  3,  4,  3,  3,-10,-10,-10,-10,-10,-10,-10,-10],
                          [  3,  3,  4,  3,  4,  3,  3,  3,-10,-10,-10,-10,-10,-10,-10,-10],
                          [  3,  4,  3,  3,  3,  3,  3,  4,-10,-10,-10,-10,-10,-10,-10,-10],
                          [  4,  3,  3,  3,  3,  3,  3,  3,  4,-10,-10,-10,-10,-10,-10,-10],
                          [  3,  4,  3,  3,  3,  3,  3,  4,  2,  2,  2,  2,  1,  1,  1,  1],
                          [  4,  3,  3,  3,  3,  3,  4,  3,  2,  2,  2,  2,  2,  2,  2,  2],
                          [  3,  3,  3,  3,  3,  4,  3,  3,  2,  2,  2,  2,  1,  1,  1,  4],
                          [  3,  3,  4,  3,  4,  3,  3,  3,  2,  2,  2,  2,  1,  1,  1,  1],
                          [-10,-10,-10,  4,  2,  2,  2,  2,  1,  1,  1,  1,  2,  4,  2,  4],
                          [-10,-10,-10,-10,  2,  2,  2,  2,  1,  1,  1,  1,  4,  2,  4,  2],
                          [-10,-10,-10,-10,  2,  2,  2,  2,  1,  1,  1,  1,  2,  4,  2,  4],
                          [-10,-10,-10,-10,  2,  2,  2,  2,  1,  1,  1,  1,  4,  2,  4,  2],
                          [-10,-10,-10,-10,  1,  2,  1,  1,  2,  4,  2,  4,  3,  3,  3,  3],
                          [-10,-10,-10,-10,  1,  2,  1,  1,  4,  2,  4,  2,  3,  3,  3,  3],
                          [-10,-10,-10,-10,  1,  2,  1,  1,  2,  4,  2,  4,  3,  3,  3,  3],
                          [-10,-10,-10,-10,  1,  2,  4,  1,  4,  2,  4,  2,  3,  3,  3,  3]]
    
    # "enumerate" user's MBTI
    if userMBTI == "infp":
        userMBTI_idx = 0 
    elif userMBTI == "enfp":
        userMBTI_idx = 1
    elif userMBTI == "infj":
        userMBTI_idx = 2
    elif userMBTI == "enfj":
        userMBTI_idx = 3
    elif userMBTI == "intj":
        userMBTI_idx = 4
    elif userMBTI == "entj":
        userMBTI_idx = 5
    elif userMBTI == "intp":
        userMBTI_idx = 6
    elif userMBTI == "entp":
        userMBTI_idx = 7
    elif userMBTI == "isfp":
        userMBTI_idx = 8
    elif userMBTI == "esfp":
        userMBTI_idx = 9
    elif userMBTI == "istp":
        userMBTI_idx = 10
    elif userMBTI == "estp":
        userMBTI_idx = 11
    elif userMBTI == "isfj":
        userMBTI_idx = 12
    elif userMBTI == "esfj":
        userMBTI_idx = 13
    elif userMBTI == "istj":
        userMBTI_idx = 14
    elif userMBTI == "estj":
        userMBTI_idx = 15
    else:
        userMBTI_idx = -1

    # "enumerate" group member MBTIs & update compatibilty score
    for groupMember in groupMBTI:
        if groupMember == "infp":
            score += compatibilityTable[userMBTI_idx][0]
        elif groupMember == "enfp":
            score += compatibilityTable[userMBTI_idx][1]
        elif groupMember == "infj":
            score += compatibilityTable[userMBTI_idx][2]
        elif groupMember == "enfj":
            score += compatibilityTable[userMBTI_idx][3]
        elif groupMember == "intj":
            score += compatibilityTable[userMBTI_idx][4]
        elif groupMember == "entj":
            score += compatibilityTable[userMBTI_idx][5]
        elif groupMember == "intp":
            score += compatibilityTable[userMBTI_idx][6]
        elif groupMember == "entp":
            score += compatibilityTable[userMBTI_idx][7]
        elif groupMember == "isfp":
            score += compatibilityTable[userMBTI_idx][8]
        elif groupMember == "esfp":
            score += compatibilityTable[userMBTI_idx][9]
        elif groupMember == "istp":
            score += compatibilityTable[userMBTI_idx][10]
        elif groupMember == "estp":
            score += compatibilityTable[userMBTI_idx][11]
        elif groupMember == "isfj":
            score += compatibilityTable[userMBTI_idx][12]
        elif groupMember == "esfj":
            score += compatibilityTable[userMBTI_idx][13]
        elif groupMember == "istj":
            score += compatibilityTable[userMBTI_idx][14]
        elif groupMember == "estj":
            score += compatibilityTable[userMBTI_idx][15]
        else:
            groupMember = -1

    #return average compatibility score user-to-groupMember
    return score/len(groupMBTI)