#클래스 : 객체를 만들어내기 위한 설계도
#객체 : 클래스에 선언된 모양 그대로 생성된 실체
#인스턴스 : 설계도를 바탕을로 소프트웨어 세계에 구현된 구체적인 실체

class Human:
    pass

class Human:
    def __init__(self):
        print("응애응애")

areum = Human()

class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def set_info(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def who(self):
        print("이름 : {} 나이 : {} 성별 : {}".format(self.name, self.age, self.sex))
    def __del__(self):
        print("나의 죽음을 알리지마라")
areum = Human("아름", 25, "여자")
print(areum.name)
print(areum.age)
print(areum.sex)

class OMG :
    def print(self) :
        print("Oh my god")

mystock = OMG()
mystock.print()