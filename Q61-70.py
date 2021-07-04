price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])
print(nums[1::2])

nums = [1, 2, 3, 4, 5]
print(nums[::-1])

interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
sep = " "
print(sep.join(interest))

sep = "/"
print(sep.join(interest))

sep = "\n"
print(sep.join(interest))

data = [2, 4, 3, 1, 5, 10, 9]
data.sort() #none을 반환, 출력안됨
print(data)

data2 = sorted(data)#원본은 변형안됨
print(data2)