class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        indexed_nums.sort(key = lambda x: x[0])
        i, high = 0, len(nums)-1
        while i < high:
            sum = indexed_nums[i][0]+indexed_nums[high][0]
            if sum > target:
                high-=1
            elif sum == target:
                return [min(indexed_nums[i][1], indexed_nums[high][1]), max(indexed_nums[i][1], indexed_nums[high][1])]
            else:
                i+=1
        return [-1, -1]


        