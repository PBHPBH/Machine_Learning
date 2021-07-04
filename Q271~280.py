import random

class Account:

    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        self.deposit_log=[]
        self.withdraw_log=[]
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1

    def get_account_num(cls):
        print(cls.account_number)

    def deposit(self, money):
        if money >=1:
            self.balance += money
            self.deposit_log.append(money)
            self.deposit_count += money
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance = (self.balance *1.01)

    def withdraw(self, amount):
        if amount < self.balance:
            self.withdraw_log.append(amount)
            self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)
a_list = []
p = Account("Park", 1000000)
k = Account('Kim', 1000)
s = Account('Song', 10000)
a_list.append(p)
a_list.append(k)
a_list.append(s)

for c in a_list:
    if c.balance >= 1000000:
        c.display_info()





