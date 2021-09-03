class BigNumberError(Exception):
    def __init__(self, msg): # 발생 시
        self.msg = msg
    def __str__(self): # except에서 처리 중 반환
        return self.msg

try:
    print("나누기 전용 계산기입니다.")
    numbers = []
    numbers.append(int(input("첫 번째 숫자를 입력하세요: ")))
    numbers.append(int(input("두 번째 숫자를 입력하세요: ")))
    print("{0} / {1} = {2}".format(numbers[0], numbers[1], numbers[2]))
except ValueError:
    print("에러! 잘못된 값을 입력했어요!")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생했슴다.")
    print(err)


try:
    print("한 자리 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("raise - 사용자 지정 msg 출력")
    print("{0} / {1} = {2}".format(num1, num2, num1/num2))
except ValueError:
    print("잘못된 값을 입력했습니다. 의도적으로 던진 에러.")
except BigNumberError:
    print("except - 사용자가 정의한 에러 BigNumberError의 except 처리 중")
finally:
    print("이용해 주셔서 감사합니다. 이 문구는 무조건 보여집니다.")