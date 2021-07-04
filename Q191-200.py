data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
#for i in data:
#    for j in i:
#        print(j*1.00014)

#for i in data:
#    for j in i:
#        print(j*1.00014)
#    print("----")

#result = []
#for i in data:
#    for j in i:
#        result.append(j*1.00014)


#result = [] #틀림 다시한번 보기
#for line in data:
#    sub = []
#    for i in line:
#        sub.append(i*1.00014)
#    result.append(sub)
#print(result)

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
#for i in ohlc[1::]:
#    print(i[3])

#for i in ohlc[1::]:
#   if i[3]>150:
#    print(i[3])

#for i in ohlc[1::]:
 #   if i[3] >= i[0]:
  #   print(i[3])

#for i in ohlc[1::]:
#    if (i[3]- i[0])>0:
#        print(i[1]-i[2])

for i in ohlc[1::]:
    print(i[3]-i[0])