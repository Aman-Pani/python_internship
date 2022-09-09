def palindrome1(word):
    if word ==word[::-1]:
        return True
    return False

def circle(x1, y1, x2, y2, r1, r2):
    distSq = (x1 - x2) **2 + (y1 - y2) **2
    radSumSq = (r1 + r2) **2
    radSubSq = (r1 - r2) **2
    if (distSq == radSumSq) or (distSq == radSubSq):
        return 1
    elif (distSq > radSumSq) or (distSq < radSubSq) or (distSq==0) :
        return -1
    else:
        return 0

def Sequential_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            print(f'Element is present at index {i}')
            break
    else:
        print("Element not found...!!!")
        
        
def wiggle_sort(nums):
    for i in range(len(nums)):
        if (i % 2 == 1) == (nums[i - 1] > nums[i]):
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
            
def insertion_sort(list1):  
    for i in range(1, len(list1)):  
        value = list1[i]  
        j = i - 1  
        while j >= 0 and value < list1[j]:  
            list1[j + 1] = list1[j]  
            j -= 1  
        list1[j + 1] = value  
    return list1  