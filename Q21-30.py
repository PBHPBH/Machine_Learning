letters = 'python'
print(letters[0], letters[2])

license_plate = "24가 2210"
print(license_plate[-4:])

string = "홀짝홀짝홀짝"
print(string[::2])

string = 'PYTHON'
print(string[::-1])

phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))
print(phone_number.replace("-",""))

url = "http://sharebook.kr"
print(url.split('.')[-1])

string = 'abcdfe2a354a32a'
result=string.replace('a', 'A')
print(result)

a="3"
b="4"
print(a+b)

print("Hi" * 3)

print('-'*80)

t1='python'
t2='java'
t3 = t1+' '+t2+' '
print(t3*4)

name1 = '김민수'
age1=10
name2='이철희'
age2=13

print('이름: {} 나이: {}'.format(name1, age1))
print('이름: {} 나이: {}'.format(name2, age2))
print(f'이름: {name1} 나이: {age1}\n이름: {name2} 나이: {age2}')

상장주식수 = "5,969,782,550"
result = int(상장주식수.replace(',', ''))
print(result)

분기 = "2020/03(E) (IFRS연결)"
print(분기.split('(')[0])
print(분기[:7])

data="   삼성전자   "
print(data.strip())