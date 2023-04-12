class Solution:
    def containsDuplicate(self, nums):
        if len(nums)>len(set(nums)):
            return True
        return False
s=[1,4,5,1]
obj=Solution()
print(obj.containsDuplicate(s))