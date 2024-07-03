# Input_list: [2, 11, 7, 15]
# target: 9
# Output: [0,2]

def target_sum_indexes(nums, target):
    index_val_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in index_val_dict:
            return [index_val_dict[complement], i]
        index_val_dict[num] = i
    return []


vals = [2, 11, 7, 15, 7, 2]
target = 9
indexes = target_sum_indexes(vals, target)
print(indexes)
