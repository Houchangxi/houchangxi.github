class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        # find out left edge
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid

        if nums[left] == target:
            st_num = left
        elif nums[right] == target:
            st_num = right
        else:
            st_num = -1

        # find out right edge
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid

        if nums[right] == target:
            end_num = right
        elif nums[left] == target:
            end_num = left
        else:
            end_num = -1
        return [st_num, end_num]

