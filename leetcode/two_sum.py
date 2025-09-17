# LeetCode: Two Sum
# Topic: Hashmap
# Source: NeetCode 150
# Solved on: 17/09/2025

def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
