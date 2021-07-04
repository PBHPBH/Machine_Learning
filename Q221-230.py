def print_reverse(input):
    print(input[::-1])

def print_score(input):
    print(sum(input)/len(input))

def print_even (input):
    for i in input:
        if i%2==0:
            print(i)

def print_keys(input):
    for i in input.keys():
        print(i)

print_keys({"이름":"김말똥", "나이":30, "성별":0})

my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
def print_value_by_key(my_dict, date):
    print(my_dict[date])

print_value_by_key  (my_dict, "10/26")

def print_5xn(input):
   for i in range(0, len(input), 5):
       print(input[i:i+5])
print_5xn("아이엠어보이유알어걸")

def printmxn(input,n):
    for i in range(0, len(input), n):
        print(input[i:i+n])
printmxn("아이엠어보이유알어걸", 3)


def calc_monthly_salary(annual_salary):
    return int(annual_salary/12)

def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)

def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)