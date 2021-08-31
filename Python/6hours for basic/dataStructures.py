# 리스트 []
firstSubway = 10
secondSubway = 20
thirdSubway = 30
subway = [10, 20, 30]

# 20이 몇 번째 요소인지? 1
print(subway.index(20))

# 삽입 함수 append, insert
subway.append("끝에 붙이기")
subway.insert(1, "중간에 쏙") # 1번 위치에 들어간다
print(subway)

# 맨 끝에서 하나씩 pop()
print(subway.pop())
print(subway)

# 같은 값이 몇 개인지 확인하기
subway.append(10)
print(subway.count(10))

# 정렬
numList = [5, 2, 4, 3, 1]
numList.sort()
print(numList) # 1, 2, 3, 4, 5
numList.reverse() # 5, 4, 3, 2, 1

# 모두 지우기
numList.clear()

# 리스트 확장
firstList = [1, 3, 2]
secondList = ['오트밀', True, 34]
firstList.extend(secondList)
print(firstList)

# 사전 Dictionary
cabinet = {3:"스프링", 100:"갤럭시"}
print(cabinet[3])
print(cabinet.get(3))
# print(cabinet[5]) # 5라는 키가 없으니 오류 발생 후 강종
print(cabinet.get(5)) # None 출력
print(cabinet.get(5, "Default Value"))
print(3 in cabinet) # Key in dic => True / False

stringCabinet = {"A-3":"4호선", "B-100":"3호선"}
print(stringCabinet["A-3"])
stringCabinet["A-3"] = "재할당된 5호선" # 이미 있는 Key라면 재할당
stringCabinet["C-20"] = "7호선" # 없는 Key라면 값 추가

del stringCabinet["B-100"] # 값 삭제
print(stringCabinet.keys()) # 키들만 출력
print(stringCabinet.values()) # 값들만 출력
print(stringCabinet.items()) # 키, 값 쌍으로 출력
stringCabinet.clear() # 모든 값 삭제

# 튜플 Tuple - 값 추가 및 변경 불가, 속도는 빠름 :)
menu = ("돈가스", "생선가스")
print(menu[0], menu[1])
(name, age, hobby) = ("고래", 20, "잠자기")
print(name, age, hobby)

# 집합 Set - 중복 X, 순서 X
mySet = {9, 7, 0, 7, 2, 7}
print(mySet) # 9, 7, 0, 2
javaProgrammer = {"유재석", "조세호", "김태호"}
pythonProgrammer = {"민찬기", "유재석"}

# 교집합
print(javaProgrammer & pythonProgrammer) # "유재석"
print(javaProgrammer.intersection(pythonProgrammer)) # "유재석"

# 합집합
print(javaProgrammer | pythonProgrammer)
print(javaProgrammer.union(pythonProgrammer))

# 차집합
print(javaProgrammer - pythonProgrammer)
print(javaProgrammer.difference(pythonProgrammer))

# python 할 수 있는 사람이 늘어났다면?
pythonProgrammer.add("나나나")

# 집합 값 삭제
javaProgrammer.remove("김태호")

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # {'커피', '주스', '우유'} <class 'set'>

menu = list(menu)
menu = tuple(menu)
menu = set(menu)

