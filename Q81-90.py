scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, b,c = scores
print(valid_score)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _, *valid_score = scores
print(valid_score)

_,*valid_score,_ = scores
print(valid_score)

temp = {}
print(type(temp))

아이스크림 = {"메로나" : 1000, "폴라포" : 1200, "빵빠레" : 1800}
아이스크림['죠스바'] = 1200
아이스크림['월드콘'] = 1500
print(아이스크림)

ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

print('메로나 가격:', ice['메로나'])


ice.pop('메로나')#del ice["메로나"]
print(ice)

ice['폴로포'] = 1300
print(ice)