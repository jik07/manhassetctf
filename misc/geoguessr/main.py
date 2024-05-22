#!/usr/local/bin/python

with open("location.txt") as f:
    location = map(float, f.read().strip().split(" "))

x2, y2 = location
x, y = map(float, input(f"Please enter the lat and long of the location: ").replace(",","").split(" "))

# increase if people have issues
if abs(x2 - x) < 0.0010 and abs(y2 - y) < 0.0010:
    with open("flag.txt", "r") as f:
        print("Correct! You have successfully determined the position of the camera.")
        print("Great job, the flag is " + f.read().strip())
else:
    print("Wrong! Try again after paying attention to the picture.")
