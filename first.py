import sys
def path(m,n):
		if(m == 1 or n == 1):
			return 1;	
			return  path(m-1, n) + path(m, n-1);
m=3
n=3
print(path(m,n))
	