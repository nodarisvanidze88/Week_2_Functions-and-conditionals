# ==
# >
# <
# >=
# <=
# !=
# is
# in
# =====================================
# nam1 = 2
# nam2 = 5
# action = "+"

# print(nam1 == nam2)
# print(nam1 > nam2)
# print(nam1 < nam2)
# print(nam1 >= nam2)
# print(nam1 <= nam2)
# print(nam1 != nam2)
# print(nam1 is nam2)
# =====================================

# def main():
#     nam1 = input("Add first number ")
#     nam2 = input("Add second number ")
#     action = input("Add action ")
#     result1, result2 = converter(nam1, nam2)

#     if action == "+":
#         print(f"{nam1} {action} {nam2} = {sumfunction(result1, result2)}")
#     elif action == "-":
#         print(f"{nam1} {action} {nam2} = {substarctionfunction(result1, result2)}")
#     elif action == "*":
#         print(f"{nam1} {action} {nam2} = {multiplyfunction(result1, result2)}")
#     elif action == "/":
#         print(f"{nam1} {action} {nam2} = {devisionfunction(result1, result2)}")
#     elif action == "avg":
#         print(f"{nam1} {action} {nam2} = {average(result1, result2)}")
#     elif action == "sqr":
#         print(f"{nam1} {action} {nam2} = {square(result1, result2)}")

# def converter(n1, n2):
#     x = float(n1)
#     y = float(n2)
#     return x, y

# def sumfunction(n1, n2):
#     return n1+n2

# def substarctionfunction(n1, n2):
#     return n1-n2

# def multiplyfunction(n1, n2):
#     return n1*n2

# def devisionfunction(n1, n2):
#     return n1/n2

# def average(n1, n2):
#     return (n1+n2)/2

# def square(n1, n2):
#     return n1**n2

# main()

# =====================================

# def main():
#     # მომხამრებელს ვკითხავ რიცხვს
#     # უნდა გარდავქმნა ინტეჯერად
#     # და გამოვპრინტო შესაბამისი grade
#     user = grades(int(input("Give us the grade score: ")))
#     print(user)

# def grades(number):
#     # თუ შემოვიდა რიცხვი 90 და მეტი მაშინ A
#     # თუ 80-90 B
#     # თუ 70-80 C
#     # თუ 60-70 D
#     # თუ არცერთი f

#     if number >= 90:
#         return f"A\nCongratulation"
#     elif number >= 80:
#         return f"B\nGood"
#     elif number >= 70:
#         return f"C\nNot Bad"
#     elif number >= 60:
#         return f"D\nAlmost there"
#     else:
#         return f"F\nYou are faild"

# main()

# =====================================

# def main():
#     height = float(input("Give the height: "))
#     width = float(input("Give the width: "))
#     dimention = input("CM or M? ")

#     result1, result2 = converter(height, width, dimention)
#     perimetrResult = perimeter(result1, result2)
#     areaResult = area(result1, result2)

#     print(f"Perimeter equal: {perimetrResult}")
#     print(f"Area equal: {areaResult}")

# def converter(length, width, dim):
#     if dim.upper() == "CM":
#         return length/100, width/100
#     else:
#         return length, width

# def perimeter(lenth, width):
#     preimetr = (lenth + width)*2
#     return preimetr

# def area(lenth, width):
#     totalarea = lenth * width
#     return totalarea

# main()

# =====================================

# def main():
#     user = input("Add your e-mail: ")

#     if mailvalidator(user):
#         print("You are registered")
#     else:
#         print("You are new person")


# def mailvalidator(txt):
#     if "@" in txt:
#         return True
#     else:
#         return False

# main()

# =====================================

# user = " "

# if user:
#     print("Hello")
# else:
#     print("Goodbay")
