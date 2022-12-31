import numpy as np
def SortData(InputArr):
    SortedArr=[]
    for Itr in range(0,len(InputArr)):
        CurrentMin=np.min(InputArr)
        CurrentMinIndex=InputArr.index(CurrentMin)
        InputArr.remove(InputArr[CurrentMinIndex])
        SortedArr.append(CurrentMin)
    print(SortedArr)
    return 0

if __name__ =="__main__":
    SortData([8,9,4,5,6,2,4,8,2,2,1,4,5,7])

#Selection Sort
