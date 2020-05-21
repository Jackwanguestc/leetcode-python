'''
给定一个整数数组 nums 和一个目标值 target，
请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
'''
import numpy as np
import logging

def two_sum(nums, target):
    # nums是数组，遍历nums，找target-nums【i】，
    if len(nums)>2:
        result = []
        for idx,value in enumerate(nums):
            for i in range(len(nums)-idx):
                if nums[idx+i] == target - value:
                    result.append((idx, idx+i))
        return result
    else:
        logging.error("nums len less than 2")
        return 0


if __name__=="__main__":
    nums = [2, 7, 11, 15, 4, 3, 5, 6, 12, 9]
    target = 15
    print(two_sum(nums, target))

