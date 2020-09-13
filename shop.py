#!/usr/bin/python3

d = {"a": 100, "b": 200, "c": 300, "d": 400}
inv = {0: ["Item", " Cost", " Nos.", "Total Cost"], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
print('Item:', end="  ")
for i in d.keys():
    print(i, end="     ")
print()
print('Cost:', end="  ")
for j in d.values():
    print(j, end="   ")
print()
print()
s = input("Select the desired item(s): ")
for k in d.items():
    if s == k[0]:
        n = int(input("Nos.: "))
        inv[1].extend([s, " ", k[1], " ", n, " ", n * k[1]])
        for e in inv[0]:
            print("      ", e, end="    ")
        print()
        print(1, ".", end="  ")
        for f in inv[1]:
            print("    ", f, end=" ")
        break
if s != k[0]:
    print("Invalid Entry!")
m = 1
def operation():
    while m <= (len(inv)-1):
        for k in d.items():
            if s == k[0]:
                n = int(input("Nos.: "))
                inv[m].extend([s, " ", k[1], " ", n, " ", n*k[1]])
                for g in inv[0]:
                    print("      ", g, end="    ")
                print()
                print(m, ".", end="  ")
                for h in inv[m]:
                    print("    ", h, end=" ")
                break
        if s != k [0]:
            print("Invalid Entry!")
        break

print()
print()
for r in range(5):
    q = input("Do you wish to continue ? ")
    if q == "yes":
        s = input("Select the desired item(s): ")
        m += 1
        operation()
        print()
    else:
        print("Thank you for Shopping.")
        break

print()
print()
#print(inv)
for g in inv[0]:
    print("      ", g, end="    ")
print()
for fin1 in range(1, len(inv)):
    print(fin1, ".", end="  ")
    for fin2 in inv[fin1]:
        print("    ", fin2, end=" ")
    print()
print()
print(" ____________________ Thank you for Shopping. _____________________")

