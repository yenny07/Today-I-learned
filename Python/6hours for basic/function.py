def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었어요. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance > money:
        print("출금 완료. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("잔액이 모자랍니다. {0} 원뿐이에요.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100 # 수수료 100원
    return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 500) # 리턴이 이렇게 올 수 있다니...

# 기본값, 키워드 값
def profile(name, age=17, main_language="python"): # 기본값 설정
    print("이름: {0} 나이: {1} 주 사용 언어: {2}"\
          .format(name, age, main_language))

profile("yeye", 25, "java")
profile("seung")
profile(name="hey", main_language="java", age=1) # 키워드로 매개변수 직접 지정

# 가변 인자
# def profile(name, age, lang1, lang2, lang3):
#     print("이름: {0}, 나이: {1}\t".format(name, age), end=" ") # 줄 바꾸지 말고 한 칸 띄기만 해라
#     print(lang1, lang2, lang3)

# 아니 근데 lang이 세 개가 안되거나 세 개 넘으면 어떻게 해? 그러니 가변 인자를 쓰자~
def profile(name, age, *languages):
    print("이름: {0}, 나이: {1}".format(name, age), end=" ")
    for lang in languages:
        print(lang, end=" ")

# 지역변수, 전역변수
gun = 10
def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun 사용
    gun -= soldiers
    print("남은 총:", gun)
