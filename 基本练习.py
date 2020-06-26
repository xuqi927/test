b = 'xuqi'
print('欢迎'+b+'光临')

a="欢迎%s光临"%'xuqi'
print(a)


a='xuqi'
c=f'欢迎{a}光临'
print(c)
print(f'欢迎{a}光临')

a='xuqi'
print('欢迎',a,'光临')
a=a*20
print(a)

a=True
a=False
b=None
print(b)

print(type(b))
a='das'
print('a的类型是',type(a))

a=4719823

a=a**0.5
print('a=',float(a))

a+=5
print(a)
a//=5
a%=54
print(a)

a=1 and 2 #1与二就是11与1
print(a)

a=123
b=233
c=627
print("最大值是a",a)if a>b else print('最大值是b',b)
d = a if a>b else b
max = d if d>c else c
print('最大值是',max)
    