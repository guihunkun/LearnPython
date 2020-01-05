#!/usr/bin/env python
# -*- coding:utf-8 -*-

# S2：变量及简单数据类型

hello = "Hello"
name = "guihun"
print(name.title())
print(name.upper())
print(name.lower())
print(hello+" "+name.title())
print(1 / 2)
print(1 // 2)
print(type(str(23)))
print(type(23))
i = 58888888888888888888
print(i)

# S3：列表
name_s3 = ["guihun", "gh", "shuxue", "sx", "good"]
name_s3.append("qu")
print(name_s3)
name_s3.insert(0, "GH")
print(name_s3)
del name_s3[3]
print(name_s3)
print(name_s3.pop())
print(name_s3)
print(name_s3.sort())
print(name_s3)
name_s3.sort()
print(name_s3)
print(sorted(name_s3))
name_s3.reverse()
print(len(name_s3))


# S4：操作列表
name_s3 = ["guihun", "gh", "shuxue", "sx", "good"]
for name in name_s3:
    print(name)

digits = [i for i in range(10)]
print([i for i in range(5)])
print(min(digits))
print(sum(digits))
print(digits[0:3])
print(digits[-3:])

digits_c = digits
digits_c.append(15)
print(digits_c)
print(digits)
digits_copy = digits.copy()
digits_copy.append(15)
print(digits_copy)
print(digits)


# S6：字典
score = {"gui": 100, "hun": 90}
print(score)
print(score["gui"])
score["shu"] = 100
print(score)
score["hun"] = 70
print(score)
del score["shu"]
print(score)
for name, sc in score.items():
    print(name)
    print(sc)
for name in score.keys():
    print(name)
for sc in sorted(score.values()):
    print(sc)


# S7：用户输入和while循环
message = input("Tell me something:")
print(message)

age = input("Tell me your age:")
age_x = int(age)
age_x += 10
print(age_x)

sum1 = 0
i = 0
while i < 101:
    sum1 += i
    i += 1
print(sum1)

print(sum([i for i in range(101)]))


# S8：函数
def get_fullname(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()

full_name = get_fullname("gui", "hun")
print(full_name)

def make_pizza(*toppings):
    print(toppings)
make_pizza("pep", "ger", "ext")


# S9：类
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


my_dog = Dog("while", 16)
my_dog.sit()
my_dog.roll_over()

class Car():
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def prixinxi(self):
        print(self.make + " " + self.model)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def prixinxi_E(self):
        print(self.year + " " + self.model)


my_car = Car("tesla", "model s")
my_car.prixinxi()
my_Ecar = ElectricCar("tesla", "model s", "2019")
my_Ecar.prixinxi_E()






