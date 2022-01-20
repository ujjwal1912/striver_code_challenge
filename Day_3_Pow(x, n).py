# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

def myPow(self, x: float, n: int) -> float:
        p = n if n>0 else n*-1
        ans=1
        while(p>0):
            if p%2:
                ans*=x
                p-=1
                print(p, ans)
            else:
                x*=x
                p/=2
                print(p, x)
        ans = ans if n>0 else 1/ans 
        return ans
