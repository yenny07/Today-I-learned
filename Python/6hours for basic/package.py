# # from . import travel.thailand : 이렇게 쓰면 안된다!!
# from .travel import thailand
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# # travel 패키지 안에 있는, thailand 모듈에서, ThailandPackage 클래스만 임포트
# from .travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# __init__에 __all__로 공개여부를 정해두지 않으면, NameError: name 'vietnam' is not defined
from .travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

import inspect
print(inspect.getfile(travel))