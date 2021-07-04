price_list = [32100, 32150, 32000, 32500]
#for i in range(0,4):
#    print(price_list[i])

#for i, a in enumerate(price_list):
#    print(i, a)

#for i, a in enumerate(price_list):
#    print(3-i, a)

#my_list = ["가", "나", "다", "라"]
#for i in range(0,3):
#    print(my_list[i], my_list[i+1])

#my_list = ["가", "나", "다", "라", "마"]
#for i in range(0,3):
#    print(my_list[i], my_list[i+1], my_list[i+2])

#my_list = ["가", "나", "다", "라"]
#for i in range(0,3):
#    print(my_list[3-i], my_list[2-i])

#my_list = [100, 200, 400, 800, 1000, 1300]
#for i in range(0,4):
#    print((my_list[i]+my_list[i+1]+my_list[i+2])/3)

volatility = []
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
for i in range(0,len(high_prices)):
    volatility.append(high_prices[i]-low_prices[i])