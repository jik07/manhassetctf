from os import mkdir, urandom
from random import randint

size = 100
base = "haystack"
flag = "mctf{n33dl3_1n_4_h4yst4ck_be36a510}"
pos = []
for i in range(len(flag)):
    pos.append([randint(0, size**3-1), str(i), flag[i]])
mkdir(base)

for i in range(size):
    a = urandom(8).hex()
    mkdir(f"{base}/{a}")
    for j in range(size):
        b = urandom(8).hex()
        mkdir(f"{base}/{a}/{b}")
        for k in range(size):
            c = urandom(8).hex()
            mkdir(f"{base}/{a}/{b}/{c}")
            for character in pos:
                if character[0] == i * size**2 + j * size + k:
                    with open(f"{base}/{a}/{b}/{c}/{character[1]}.txt", "w") as f:
                        f.write(character[2])