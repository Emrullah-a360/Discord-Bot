import random

def gen_pass(uzunluk_sayisi):
    karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    sifre = ""
    for i in range(uzunluk_sayisi):
        sifre += random.choice(karakterler)
    return sifre
