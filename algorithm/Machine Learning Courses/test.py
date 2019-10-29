class Solution(object):
    def test(self, x):
        print('123')
        print('1')
        return 'a'

    def countdown(self, n):
        if n <= 0:
            print('Blastoff')
        else:
            print(n)
            self.countdown(n - 1)
    def rec(self,n,s):
        if n==0:
            print(s)
        else:
            self.rec(n-1,n+s)

    def ge

print(Solution().test(2))


# Solution().countdown(10)
Solution().rec(5,0)




