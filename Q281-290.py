class 차:
    def __init__(self, number, number2):
        self.바퀴 = number
        self.가격 = number2

    def 정보(self):
        print("바퀴수", self.바퀴)
        print("가격", self.가격)

class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        self.구동계 = 구동계
        super().__init__(바퀴, 가격)
    def 정보(self):
        super().정보()
        print("구동계", self.구동계)


class 자동차(차):
   def __init__(self,바퀴, 가격):
       super().__init__(바퀴, 가격)

class 부모:
  def 호출(self):
    print("부모호출")

class 자식(부모):
  def 호출(self):
    print("자식호출")

나 = 자식()
나.호출()

class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()