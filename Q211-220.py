#def 함수(문자열) :
#    print(문자열)
#함수("안녕")
#함수("Hi")

#def 함수(a, b) :
#    print(a + b)

#함수(3, 4)
#함수(7, 8)

#def 함수(문자열) :
#    print(문자열)
#함수()
#입력값이 없기 때문이다

#def print_with_smile(input):
#    print(input+":D")

#print_with_smile("안녕하세요")

def print_upper_price(now_price):
    print(now_price*1.3)

def print_sum(a, b):
    print(a+b)

def print_arithmetic_operation(a, b):
    print(a,"+",b,"=",a+b)
    print(a, "-", b, "=", a - b)
    print(a, "*", b, "=", a * b)
    print(a, "/", b, "=", a / b)

def print_max(a, b, c):
    max_val=a
    if b>max_val:
        max_val=b
    if c>max_val:
        max_val =c
    print(max_val)

print_max(-3,-10, -1)


