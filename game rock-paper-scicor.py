import random

hoi = str(input("Bạn có muốn chơi ko? yes để chơi tiếp, no để ko chơi: "))
while hoi == "yes":
    traloi = str(input("Bạn chon ra kéo hay búa hay bao: "))
    luachon = ["keo", "bua", "bao"]
    ketqua = random.choice(luachon)

    if traloi == ketqua:
        print("Bạn và máy hòa")
    elif (traloi == "bua" and ketqua == "keo") or (traloi == "bao" and ketqua == "bua") or (traloi == "keo" and ketqua == "bao"):
        print("Bạn đã thắng")
    else:
        print("Bạn đã thua")
    hoi = str(input("Bạn có muốn chơi lại ko? yes để chơi tiếp, no để ko chơi: "))
