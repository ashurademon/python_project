import random

Batdau = str(input("Bạn có muốn chơi ko :))),Nhập yes để chơi,No để  ko chơi: "))
while Batdau == "yes":
    dapan = random.randint(1, 100)
    print(dapan)
    traloi = int(input("Đố bạn tôi đang nghĩ số gì: "))
    while traloi != dapan:
        if traloi > dapan:
            print("Số tôi nghĩ nhỏ hơn")
        else:
            print("số tôi nghĩ lớn hơn")
        traloi = int(input("Đố bạn tôi đang nghĩ số gì: "))
    print("bạn nghĩ giống tôi đó")
    Batdau = str(input("Bạn có muốn chơi ko :))),Nhập yes để chơi,No để  ko chơi"))
