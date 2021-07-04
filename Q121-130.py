#money = {'달러': 1167, '엔': 1.096, '유로': 1268, '위안': 171}
#a = input(" 입력: ")
#if a.split()[1] == '달러':
#    print(int(a.split()[0]) * 1167, '원')
#elif a.split()[1] == '엔':
#    print(int(a.split()[0]) * 1.096, '원')
#elif a.split()[1] == '유로':
#    print(int(a.split()[0]) * 1268, '원')
#elif a.split()[1] == '위안':
#    print(int(a.split()[0]) * 171, '원')
#else :
#    print("제대로 된 형식을 입력해주세요")

#num1 = input("input number1: ")
#num2 = input("input number2: ")
#num3 = input("input number3: ")
#print(max(num1, num2, num3))

#PN = input("휴대전화 번호 입력: ")
#if PN.split("-")[0]=='011':
#    com = 'SKT'
#    print(f"당신은 {com} 사용자입니다.")
#elif PN.split("-")[0] == '016':
#    com = 'KT'
#    print(f"당신은 {com} 사용자입니다.")
#elif PN.split("-")[0] == '019':
#    com = 'LGU'
#    print(f"당신은 {com} 사용자입니다.")
#elif PN.split("-")[0] == '010':
#    print("당신의 휴대폰 회사는 알 수 없습니다.")


#a = input(" 우편번호: ")
#if a[2]=='0' or a[2]=='1' or a[2]=='2':
#    print("강북구")
#elif a[2] == '3' or a[2]=='4' or a[2]=='5':
#    print("도봉구")
#elif a[2] == '6' or a[2]=='7' or a[2]=='8' or a[2]=='9':
#    print('노원구')
#

#a = input(" 주민등록번호: ")
#if a.split('-')[1][0] =='1' or a.split('-')[1][0]=='3':
#    print('남자')
#elif a.split('-')[1][0] == '2' or a.split('-')[1][0]=='4':
#    print('여자')

#a = input(" 주민등록번호: ")
#if 0<= int(input.split('-')[1][1:3])=<8:
#    print('서울입니다.')
#else : print('서울이 아닙니다.')

#a = input(" 주민등록번호: ")
#forth = a.split('-')[0]
#back = a.split('-')[1]
#forth_sum = int(forth[0])*2 + int(forth[1])*3 + int(forth[2])*4 + int(forth[3])*5 + int(forth[4])*6 + int(forth[5])*7
#back_sum = int(back[0])*8 + int(back[1])*9 + int(back[2])*2 + int(back[3])*3 +int(back[4])*4 + int(back[5])*5
#total_sum = forth_sum + back_sum
#num=total_sum % 11
#final = int(a.split('-')[1][-1])
#if final != 11- num:
#    print("유효하지 않은 주민등록번호입니다.")
#else :
#    print("유효한 주민등록번호입니다.")

