// https://leetcode.com/problems/can-place-flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        for i in range(0,len(flowerbed)-1):
            if flowerbed[0]==0:
                if flowerbed[i]==0 and flowerbed[i+1]==1:
                    count=count+1
            else:
                if flowerbed[i]==1 and flowerbed[i+1]==0:
                    count=count+1
                
            
        print(count)
        return count==n
        
        