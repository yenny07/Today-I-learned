# 내장함수
# input
language = input("무슨 언어를 좋아하세요?: ")

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
import random
print(dir()) # 쓸 수 있는 패키지들
print(dir(random)) # 패키지 내 함수들
lst = [1, 2, 3]
print(dir(lst)) # 변수가 쓸 수 있는 함수들

# 외장함수
# glob : 경로 내의 폴더 / 파일 목록 조회 (왼도우의 dir)
import glob
print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리 출력

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성했습니다.")

# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%y-%m-%d %h:%m:%s"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

today = datetime.date.today()
day100 = datetime.timedelta(days=100) # 두 날짜 사이 간격
print("우리가 만난 지 100일 되는 날은", today + day100)