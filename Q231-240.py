def n_plus_1 (n) :
    result = n + 1

n_plus_1(3)
#print (result)#함수 정의 내의 변수이므로 외부에서 건드릴수없다

def make_url(input):
    print("www."+input+".com")


def make_list(input):
    list = []
    for i  in input:
        list.append(i)
        return list

def make_list(input):
    return list(input)

def pickup_even(input):
    list=[]
    for i in input:
        if i%2 == 0:
           list.append(i)
    return list

def convert_int(input):
    return int(input.replace(",",""))

def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)


def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)

def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)
c = 함수2(10)
print(c)


def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)