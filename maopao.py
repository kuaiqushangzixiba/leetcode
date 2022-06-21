#maopao
from subprocess import HIGH_PRIORITY_CLASS


List = []
def maopao():
    for i in range(1,len(List)):
        for j in range(0,len(List)-i):
            if List[j]>List[j+1]:
                List[j], List[j+1] = List[j+1],List[j]
    return List


#kuaisupaixu
def quick_sort(list):
    n = len(list)

    left,right = low , high
    k = list[low]
    while left<right:
        while list[right]>k:
            right -=1
        while list[left]<=k:
            left += 1
        if leftright:
            list[right],list[left] = list[left],list[right]
        
        
    
