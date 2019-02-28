class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = ()
        hashdict ={}
        if len(nums)<3 :
            return None
        
        for num in nums:
            hashdict[num] = hashdict.get(num,0)+1
        nodup_nums=list(hashdict.keys());
        
        if 0 in hashdict and hashdict[0] >= 3:
            result.append([0, 0, 0])
        
        for i, num in enumerate(nodup_nums):
            for j in nodup_nums[i+1:]:
                if num*2 + j == 0 and nhashdict[num] >= 2:
                    result.append([num, num, j])
                if j*2 + num == 0 and hashdict[j] >= 2:
                    result.append([j, j, num])
                
                dif = 0 - num - j
                if dif > j and dif in hashdict:
                    result.append([num, j, dif])
        return result