from decimal import *
from Crypto.Util.number import *

getcontext().prec = 400
N = int(5032507276169969207880317823472369228981422835058120444937042770293428269776762580279996576467663173055752796677644840268513043782101770218319909955969467)

e = int(3)
c = int(18256338817813162827232135439449533149990655997122432525319589496675918098200930057463416803520150513793810921285047483192)
for i in range(0, 10000):
    print(i)
    try:
        # 3533
        tmp = round((c+i*N)**(Decimal(1)/(3)))
        abc = long_to_bytes(tmp).decode()
        print(abc)
        break
    except:
        continue
