class Solution(object):


    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0,len(nums)-1
        mid = (r+l)//2
        left_min = self.helper(nums,l,mid)
        right_min = self.helper(nums,mid+1,r)
        return left_min if left_min<right_min else right_min

    def helper(self,nums,l,r):
        while l<r:
            mid = (r+l)//2
            if nums[mid]<nums[mid+1]:
                r = mid
            else:
                l=mid+1
        return nums[l]

s = [3,4,5,1,2]
print(Solution().findMin(s))