def has_33(nums):
    return any(nums[i] == nums[i+1] == 3 for i in range(len(nums) - 1))

print(has_33([1, 3, 3]))  
print(has_33([1, 3, 1, 3]))  
print(has_33([3, 1, 3]))  

# nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
# print(has_33(nums))