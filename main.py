#1-misol
ism = input("Ismingizni kiriting: ")

print((f"Salom, {ism}! Python dunyosiga xush kelibsiz!"))

#2-misol
yosh = int(input("Yoshingizni kiriting: "))

print((f"2026: {yosh} yosh"))


#3-misol
son = int(input("raqamni kiriting: "))

if son  % 2 == 0:
    print("Bu son juft")
else:
    print("Bu son toq")

#4-misol
a = int(input("1-raqamni kiriting: "))
b = int(input("2-raqamni kiriting: "))
c = int(input("3-raqamni kiriting: "))

eng_katta = max(a, b, c)
print("Eng katta raqam:", eng_katta)
