class Solution(object):
    def plusMinus(self, nums):

        return self.helper(nums[1:],nums[0],"")


    def helper(self, nums,num,str):
        if len(nums) == 0 and num == 0:
            print("in : ",str)
            print(num)
            return str
        elif len(nums) == 0:
            # print("in : ",str)
            # print(num)
            return 0
        # print(str)
        str_minus = str + "-"
        str_plus = str + "+"
        return self.helper(nums[1:],num-nums[0],str_minus) or self.helper(nums[1:],num+nums[0],str_plus)

numbers = [2,6,7,1,2]
print("result : ",Solution().plusMinus(numbers))

class Solution1(object):
    def plusMinus(self, nums):

        def helper(nums, num, str):
            if len(nums) == 0 and num == 0:
                print("in : ", str)
                print(num)
                return str
            elif len(nums) == 0:
                # print("in : ",str)
                # print(num)
                return 0
            # print(str)
            str_minus = str + "-"
            str_plus = str + "+"
            return helper(nums[1:], num - nums[0], str_minus) or helper(nums[1:], num + nums[0], str_plus)

        return helper(nums[1:],nums[0],"")




numbers = [2,6,7,1,2]
print("result : ",Solution1().plusMinus(numbers))