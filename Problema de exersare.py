x=[1,2,3,4,5,6,7,8,9,10,12,0]
print('Lista1', x)
y=sorted(x)
print('Lista2', y)
y.sort(reverse=True)
print('Lista3', y)
print(len(y))
print(max(y))
print(min(y))
x.extend([111])
print('Lista 4', x)
x[1]=222
print('Lista 5', x)