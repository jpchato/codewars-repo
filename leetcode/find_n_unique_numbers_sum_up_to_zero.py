'''
https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
https://donic0211.medium.com/leetcode-1304-find-n-unique-integers-sum-up-to-zero-6e5e0d4a08bd
'''
from unicodedata import name


class Solution:
    def sumZero(self, n: int):
        ans = []
        for i in range(1, n//2+1):
            ans.append(i)
            ans.append(-i)
        if n % 2 != 0:
            ans.append(0)
        print(ans)
        return ans

s = Solution()
s.sumZero(3)

def test_sumZero():
    assert s.sumZero(5) == [1, -1, 2, -2, 0]
    assert s.sumZero(3) == [1, -1, 0]
    assert s.sumZero(1) == [0]
    
if __name__ == "__main__":
    
    test_sumZero()
    print("Everything passed")