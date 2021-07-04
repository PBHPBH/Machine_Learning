my_variable = ()
print(type(my_variable))

movie_rank = "닥터 스트레인지", "스플릿", "럭키"
print(type(movie_rank))

t = ('1', '2', '3')
#t[0]='a'# 튜플은 원소의 값을 변경할 수 없다

t = 1, 2, 3, 4 #튜플이다

t = ('a', 'b', 'c')
t1 = 'A', 'b', 'c'
t=t1
print(t)

interest = '삼성전자', 'LG전자', 'SK Hynix'
data = list(interest)
print(type(data))

interest = ['삼성전자', 'LG전자', 'SK Hynix']
data = tuple(interest)
print(type(data))

temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a,b,c)

data = tuple(range(2, 100, 2))
print(data)
print(type(data))
