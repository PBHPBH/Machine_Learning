import csv
f = open("C:/Users/gjsdl/Desktop/매수종목1.txt", mode = "wt", encoding="utf-8")
f.write("005930\n")
f.write("005380\n")
f.write("035420")
f.close()

f = open("C:/Users/gjsdl/Desktop/매수종목2.txt", mode = "wt", encoding="utf-8")
f.write("005930 삼성전자\n")
f.write("005380 현대차\n")
f.write("035420 NAVER")
f.close()

#f = open("C:/Users/gjsdl/Desktop/매수종목.csv", mode="wt", encoding="cp-949", newline=" ")
#writer = csv.writer(f)
#writer.writerow(["종목명", "종목코드", "PER"])
#writer.writerow(["삼성전자", "005930", 15.79])
#writer.writerow(["NAVER", "035420", 55.82])
#f.close()

f = open("C:/Users/gjsdl/Desktop/매수종목1.txt", encoding = "utf-8")
lines = f.readlines()

codes = []
for line in lines:
    code = line.strip()
    codes.append(code)

print(codes)
f.close()


f=open("C:/Users/gjsdl/Desktop/매수종목2.txt", encoding = "utf-8")
lines = f.readlines()

data = {}
for line in lines:
    line = line.strip()
    k, v = line.split()
    data[k]=v

print(data)
f.close()



per = ["10.31", "", "8.00"]
new_per = []

for i in per:
    try:
       v = float(i)
    except:
       v=0

    new_per.append(v)
print(new_per)


try:
    b = 3 / 0
except ZeroDivisionError:
    print("0으로 나누면 안되요")


data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)

per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")

