class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 123456
        # 612345
        # 561234
        # 456123
        # 345612
        # 234561
        n = len(nums)
        l = 0
        r = n-1
        while l<=r:
            mid = (l + r) // 2
            if target == nums[mid]: return mid
            # when left side is sorted
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # when right side is sorted
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                     l = mid + 1
        return -1