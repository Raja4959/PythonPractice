#  find all unique triplets in the list that sum up to zero
def triplets(nums: list):
    # Sort the array to easily skip duplicates
    nums.sort()
    triplets = []

    # Iterate over the array
    for i in range(len(nums) - 2):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Two pointers approach to find two numbers that sum up to -nums[i]
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                # Found a triplet that sums up to zero
                triplets.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return triplets


# input = [0, -1, 2, -3, 1]
# input = [-1, 0, 1, 2, -1, -4]
input = [-1, -2, 0, 1, 2, 3, -3, -1, -2, -4]
output = triplets(input)
print(output)
