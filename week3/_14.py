def spy_game(nums):
    return [0, 0, 7] in [nums[i:i+3] for i in range(len(nums)-2)]

nums = list(map(int, input("Enter numbers: ").split()))
print(spy_game(nums))