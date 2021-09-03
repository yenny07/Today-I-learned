class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 50만원")

if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행했습니다.")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 이 모듈을 import하여 호출했습니다.")