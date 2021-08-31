# 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5 + 3)
print(2 * 8)

# 문자 자료형
print('풍선')
print("나비" * 3)

# Boolean
print(5 > 10)
print(True)
print(False)
print(not True)
print(not (5 > 10))

# 반려동물을 소개해 주십쇼.
animal = "고앵이"
name = "겨울이"
age = 6
hobby = "먹는 것"
isAdult = age > 3

print("우리집 " + animal + "의 이름은 " + name + "에요.")
print(str(age) + "살이고 " + hobby + "을 너무 좋아해요.")
print(name, "는 어른일까요?", str(isAdult))  # ,는 띄어쓰기 자동삽입되고 string이 아닌 변수 형변환 안 해도 됨

# 연산자
print(2 ** 3)  # 2^3 = 8
print(5 % 3)  # 나머지인 2
print(10 % 3)  # 1
print(10 // 3)  # 몫인 3

print(10 > 3)
print(4 >= 7)
print(3 == 3)
print(4 != 1)
print(not (1 != 3))  # False
print((3 > 0) and (3 < 5))  # &
print((3 > 0) or (3 > 5))  # |
print(5 > 4 > 7)  # False

# 수식
number = 2 + 3 * 4
number = number + 2
print(number)
number += 2  # *= -= /= %=
number %= 4
print(number)

# 숫자 처리 함수
print(abs(-5))  # 5
print(pow(4, 2))  # 4^2 = 16
print(max(5, 12))  # 12
print(min(5, 12))  # 5
print(round(3.14))  # 반올림 => 3
print(round(4.99))  # 5

from math import *
print(floor(4.99))  # 내림 -> 4
print(ceil(3.01))  # 올림 -> 4
print(sqrt(16))  # 제곱근 -> 4

from random import *
print(random())  # 0.0 이상 1.0 미만의 임의의 값 생성
print(random() * 10)  # 0.0 이상 10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값... 소수점 보기 싫다!
print(int(random() * 10) + 1) # 1부터 10이하의 임의의 값!!
print(int(random() * 45) + 1) # 1~45 이하의 임의 값. 로또 번호.
print(randrange(1, 46)) # 1~46 미만의 임의 값.
print(randint(1, 45)) # 1~45 이하의 임의 값

# 문자열
sentence = '나는 소년이다.'
print(sentence)
sentence2 = "쌍따옴표로 나는 소년이다."
print(sentence2)
sentences = """나는 소년이고,
이건 여러 줄 문장이고,
신기하네...."""
print(sentences)

# Slicing
idNumber = "990120-1234567"
print("성별 : " + idNumber[7]) # 문자열 인덱스 0부터 시작
print("연 : " + idNumber[0:2]) # 0부터 2 직전까지 0, 1번째
print("월 : " + idNumber[2:4]) # 2부터 4 직전까지 3, 4번째
print("생년월일 : " + idNumber[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + idNumber[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤에부터) : " + idNumber[-7:]) # 맨 뒤에서 7번째부터 끝까지

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))
print(python.index("n")) # 5
print(python.index("n", 6)) # 6번째 자리 그 뒤부터 찾아라~ 15
print(python.find("Java")) # 값이 없으니 -1
# print(python.index("Java")) # 에러
print(python.count("n")) # 2번 나온다

# 문자열 포맷
# 방법 1
print("정수 포맷 %d" % 20)
print("문자열 포맷 %s" % "메롱메롱")
print("캐릭터 포맷 %c" % "A")
print("나는 %s색과 %s색을 좋아해요." %("초록", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("얘는 중괄호를 두 개 {} {} 쓰면 돼요.".format("이렇게", "저렇게"))
print("얘는 중괄호를 두 개 {0} {1} 쓰면 돼요.".format("{0}에 쏙", "{1}에 쏙"))

# 방법 3
print("나는 {age}살 이며, {color}색을 좋아해요.".format(age = 25, color="초록"))

# 방법 4 (v3.6 이상~)
age = 25
color = "초록"
print(f"나는 {age}살 이며, {color}색을 좋아해요.")

# 탈출 문자
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")
# \' \" : 문장 내 따옴표
print("마치 'C언어'를 처음 배울 때 같네요.")
print('마치 "C언어"를 처음 배울 때 같네요.')
print("마치 \"C언어\"를 처음 배울 때 같네요.")
print("마치 \'C언어\'를 처음 배울 때 같네요.")
# \\ : 문장 내에서 \
print("D:\\Today-I-learned\\Python\\venv\\Scripts\\python.exe")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")
