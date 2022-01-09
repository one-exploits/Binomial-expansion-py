# Python 3 program To calculate 
# The Value Of nCr
def nCr(n, r):
    return (fact(n) / (fact(r) 
                * fact(n - r))) 
# Returns factorial of n
def fact(n): 
    res = 1
    for i in range(2, n+1):
        res = res * i
    return res

n=int(input("n :"));
r=0;
while(r<=n):
	print("n={} && r={}------>{}C{}=={}".format(n,r,n,r,nCr(n,r)));
	r=r+1  
