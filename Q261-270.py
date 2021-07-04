class Stock :
    def __init__(self,name,code, PER, PBR, 배당수익률):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.배당수익률 = 배당수익률
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
    def set_per(self, PER):
        self.PER = PER
    def set_pbr(self, PBR):
        self.PBR = PBR
    def set_dividend(self, 배당수익률):
        self.배당수익률=배당수익률

t = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
t.set_per(12.75)

t = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
p = Stock("현대차", "005380", 8.70, 0.35, 4.27)
s = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

list_ = []
list_.append(t)
list_.append(p)
list_.append(s)

for i in list_:
    print(i.code, i.PER)

