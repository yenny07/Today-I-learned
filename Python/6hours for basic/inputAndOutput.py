import sys
print("Python", "Java", sep=",") # sperator가 있었던 거임... 기본 값이 " "였던 거임..!!!! 세상에
print("Python", "Java", "JavaScript", sep=" vs ", end=": ") # Python vs Java vs JavaScript:
# print("Heyyyy", "Youuuu", file=sys.stdout) # 표준 출력
# print("Heyyyy", "Youuuu", file=sys.stderr) # 표준 에러

# 출력문 정렬
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") # 8칸확보&왼쪽정렬, 4칸확보&오른쪽 정렬

for num in range(1, 6):
    print("대기번호 : " + str(num).zfill(3)) # 3칸확보&빈공간은 0으로

# 표준 입력
answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) #class 'str' 사용자 입력은 항상 문자열로 저장된다.
print("입력하신 값은 " + answer + "입니다.")

# 출력 포맷
# 빈 자리는 빈 공간으로 두고( ), 오른쪽 정렬(>), 총 10자리 확보
print("{0: >10}".format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500)) # +500
# 왼쪽 정렬, 빈칸을 밑줄로 대체
print("{0:_<+10}".format(500))
# 세 자리마다 콤마 찍기, 부호 붙이기, 자리 수 확보, 빈자리는 ^로 채우기
print("{0:^<+20,}".format(100000000))
# 소수점 특정 자리 수까지만 출력
print("{0:.2f}".format(5/3)) # 1.67

# 파일 입출력
# w: 덮어 쓰기
# a: 덧붙이기
# r: 읽기
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 100", file=score_file)
score_file.close()

# 한 줄 씩 읽기
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline() # 한줄 만 읽고, 커서는 그 다음 줄로 이동
    if not line:
        break
    print(line, end="")
# line_list = score_file.readlins() # 줄 당 하나씩 리스트로 저장
score_file.close()

# pickle
import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름":"유재석", "나이":30, "취미":["아보카도 키우기, 제빵, 코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # fild에 있는 내용을 profile에 불러오기
print(profile)
profile_file.close()

# with
with open("profile.pickle", "rb") as profile_file: # 파일을 열어서 profile_file에 저장
    print(pickle.load(profile_file)) # profile_file을 로드해 출력

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파일을 두 문장으로 써보기 wow")
