#maopao



List = []
def maopao():
    for i in range(1,len(List)):
        for j in range(0,len(List)-i):
            if List[j]>List[j+1]:
                List[j], List[j+1] = List[j+1],List[j]
    return List


#kuaisupaixu
# coding=utf-8
def quick_sort(array, start, end):
    if start >= end:
        return
    mid_data, left, right = array[start], start, end
    while left < right:
        while array[right] >= mid_data and left < right:
            right -= 1
        array[left] = array[right]
        while array[left] < mid_data and left < right:
            left += 1
        array[right] = array[left]
    array[left] = mid_data
    quick_sort(array, start, left-1)
    quick_sort(array, left+1, end)
 
 
if __name__ == '__main__':
    array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
    quick_sort(array, 0, len(array)-1)
    print(array)
        
        
    
