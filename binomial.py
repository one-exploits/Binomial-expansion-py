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


def binomial(x,a,power):
	r=int();
	r=0;
	while(r<=power):
		T_r_pls_1=(nCr(power,r))*(x**(power-r))*((a**r));
		print("{}th term of expansion ={}".format(r+1,T_r_pls_1))
		#ans=T_r_pls_1%12;
		#print(ans);	
		r=r+1;
x=float(input("x :"));
a=float(input("a :"));
power=int(input("n :"));
binomial(x,a,power);
n = 1000
r =60
#print(int(nCr(n, r)))