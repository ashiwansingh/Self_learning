# Maximum Number of Activities

# You are given activities with their start and finish times.

# Select the maximum number of non-overlapping activities.
start  = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

def activitySelection(start, finish):
    lastStart = start[0]
    lastFinish = finish[0]


    for i in range(len(finish)):
        if lastStart>= lastFinish:
            count +=1        

            
    return 

print(activitySelection(start , finish))