class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """            
        index =0;
        dictdata = {}
        while index <( len(nums)-1):
            dictdata[nums[index]]=index
            
            index = index +1
            tmp = target -nums[index]
            
            if tmp in dictdata.keys() :
                return[ dictdata[tmp],index]
          
        return None