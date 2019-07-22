r,f,t=input().split()
x=int(r)
y=int(f)
z=int(t)
if (x>y and x>z):
	print(x)
elif(y>x and y>z):
	print(y)
else:
	print(z)
