import numpy as np

data = np.cos(np.arange(20)).reshape(5,4)
print(data)
print(np.argmax(data,axis=0))
print(np.argsort(data,axis=0))
print(np.sort(data,axis=0))


x = np.array([1,2,3])
y = np.array([4,5,6])
print(np.ones((3,2)))
print(np.zeros((5,6)))
print(np.linspace(0,4,9))
print(np.eye(3))
n = np.array([3,4,5])
print(np.diag(y))
print(np.array([1,2,3]*3))
print(np.repeat([1,2,3],3))
print(np.ones([2,3],int))
p = np.ones([2,3],int)
print(np.hstack([p,2*p]))
print(x+y)
print(x*y)
print(x**2)
print(x.dot(y))

z = np.array([y,y**2])
print(z.shape)
print(z.T.shape)
print(z.dtype)
print(z.astype('f').dtype)
a = np.array([-4,-3,1,-2,6,7])
print(a.sum())
print(a.max())
print(a.min())
print(a.mean())
print(a.std())
print(a.argmax())
print(a.argmin())

# Indexing / Slicing
a = np.arange(13)**2
print(a)
print(a[0],a[4],a[0:6])
print(a[-6:])
r = np.arange(36)
r.resize((6,6))
print(r)
print(r[2,2])
print(r[3,3:6])
print(r[r>30])
r[r>30] = 30
print(r)
r2 = r[:3,:3]
print(r2)
r2[:] = 0
print(r2)
print(r)
r_copy = r.copy()
r_copy[:]= 10
print(r_copy)
print()
print(r)


# Iterating Over Arrays
test = np.random.randint(0,10,(3,4))
print(test)
for row in test:
    print(row)
print()
for i in range(len(test)):
    print(test[i])

print()

for i,row in enumerate(test):
    print('row ', i , 'is ',row)
test2 = test**2
for i,j in zip(test,test2):
    print(i,'+',j,'=',j+i)

diag_test = np.arange(36)
diag_test.resize((6,6))
print(diag_test)
print(diag_test[::,:7])