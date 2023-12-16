import random

angka = random.randint(1, 30)

while True:
    tebak = int(input("Yuk tebak angka dari 1-30: "))

    if tebak == angka:
        print("Wahh benar! Kamu dukun yaaaa?")
    else:
        print("Yahh, salahhhh")