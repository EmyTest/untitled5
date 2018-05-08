# a = int(2.99)
# print(a)
#
# totalinches = 41
# feet = totalinches //12
# inches = totalinches % 12
# # print(feet,inches)
#
# a = 5
# b = 3
# print(round(a/b))

# reverse = 98456
# costs = 45000
# profit = reverse - costs
# print(profit)

# p_water = 1600
# p = 315000000
# t = 365
# s = p_water * p * t
# print(s)

#
#
# a = 'str1'
# print(len(a))

# praise = "good doggie".upper()
# numberOfGees = praise.count('G')
#
# numberOfGees = "good doggie".upper().count('G')
# # print(numberOfGees)
#
# fullname = input("enter a fullname: ")
# n = fullname.rfind(" ")
# print("last name: " , fullname[n+1:])
# print("first name(s):",fullname[:n])
#
# age1 = int(input("enter your age: "))
# age2 = float(input("enter your age: "))
# age3 = eval(input("enter your age: "))
# print(age1,age2,age3)

# print("Computer".find('E'))


#

# a ="king lear".title()
# print(a)

# b="8 Ball".lower()
# print(b)

# a = print(input("please enter some string:"))
# b = str(a)
# c = b[:-2]
# print(c)

# a = "eggs"
# print(a[1:])

# phonenumber = "234-5678"
# print("my phone number is " + phonenumber)

# ####
# quoto = "i came to casablance for the waters"
# print(quoto + ":"+"bogart")
#
# print(type('say it aint so.'))
# print(type("say it aint so."))

# firstName = "thomas"
# middleName = "Alva"
# lastName = "Edison"
# yearOfBirth = "1847"
# print(firstName,middleName,lastName+","+  yearOfBirth)
#
# publisher = "pearson"
# print("(c)" + publisher)
#
# a = print(input("distance stoem (miles): " ))
# b = a/5
# print("lighting and thunder: "+b )


# prompt = "enter number of seconds between lighting and thunder: "
# numberOfSecond = float(input(prompt))
# distance = numberOfSecond / 5
# dinstance = round(distance,2)
# print("distance from storm:",distance,"miles")
#
# a = "please enter some string:"
# b = str(input(a))
# print(b[:-1])
#
#
# a = "enter of hours cycling: "
# b = "enter of hours running: "
# c = "enter of hours swimming: "
# a1 = float(input(a))
# b1 = float(input(b))
# c1 = float(input(c))
# total = (a1*200 + b1*475 + c1*275) / 3500
# print("weight loss: ",total,"ponds")

# kph = "enter speed in kph"
# kp = float(input(kph))
# mph = round(kp*0.6214,2)
# print("speed in mph: ",mph )
# number = input("enter number")
# decimalpoint = number.find('.')
# print(decimalpoint)
# print(decimalpoint,"digits to left of decimal point")
# print(len(number) - decimalpoint - 1,"digits to right decimal point")

#
# str1 = "Runoob example....wow!!!"
# str2 = "exam";
#
# print(str1.find(str2))
# print(str1.find(str2, 5))
# print(str1.find(str2, 10))


# with open('yourfile.txt','rw') as f:
#     s = f.read()
#     s.replace('oldword', 'newword')
#     f.write(s)

##############################

# a =input(" enter some words: ")
# print(type(a))
# b = input(" enter one word: ")
# c =input(" enter the replacement word: ")
# d = a.replace(b,c)
# print(d)
#
#
# print("hello" ,"world",sep="^^^^")
# print("hello",sep="^^^^^^")
# print("hello",end="       #")


# print(len("a\tc"))
# print("a\nc")



# print('3'.center(5),"babe ruth".ljust(20),"714".rjust(3),sep="*")

# str1 = "zxcvbnmn"
# # print("{0:<ws}".format(str1))
# # print("{0:^ws}".format(str1))
# # print("{0:>ws}".format(str1))
# print(str1.ljust(w))



# print("the area of {0:s} is {1:d} square miles.".format("texts",268820))
# a =['c','gg']
# b = a.reverse()
# print(b)
#
# print("he said\"how ya doin ?\" to me")
# print('he said "how ya doin?" to me.')
#
# print("01234567890123456")
# # print("{0:^7s}{1:4


#
# bill = float(input("enter amount of bill: "))
# tip = float(input("enter percentage tip: "))
# tip = (bill*tip)/100
# print("tip:${0:.2f}".format(tip))


#注意幂次方的表示“**”
# p = float(input("enter principal: "))
# r = float(input("enter interest rate (as %): "))
# n = float(input("enter number of year: "))
# f = p*((1+(r/100))** n)
# print("future value: {0:.2f}".format(f))


#
# print("a,b,c".split(','))
# print("a**b**c".split('**'))
# print("a b c".split())
'''
split方法:将字符串变成其子串组成的列表
'''
from re import split

'''
join方法： 将一个字符串列表变成一个字符串
'''
# line = ["to","be","or","not","to","be"]
# print("".join(line))
# print(",".join(line))



# list1 = ['a','b']
# list2 = list1
# list2[1] = 'c'
# print(list1)

#
# a = 2
# b = 3
# # print(())
#
# s = "".join(['a','b'])
# print(s)
# print(type(s))
# s1 = 'a'+'b'
# # print(s1)
# # print(type(s1))
#
# states = ["aaaaaa","bbbbbbb","cccc","dddddd","eeeeeeee","fffffffff","gggg","hhhhhhh","iiiiiiii","jjjjjjjjj","kkk"]
# states.append(["puerto rico"])
# print(states)
#
#
# l = ["sentence","contains","five","words"]
# l.insert(0,"this")
# print(" ".join(l))
# del l[3]
# l.insert(3,"six")
# # l.insert(4,"different")
# # print(" ".join(l))
#
#
# name = input("enter name with three parts: ")
# l = name.split()
# print(l)
# print("middle name: ",l[1])


# threeRs = ["reading","writing","rithmetic"]
# print(threeRs[2])


# word = "sea"
# b = word.index("e")
# print(b)
# # # word[0] = 'p'
# # # print(word)
#
# list1 = ["1","two","three","4"]
# print(" ".join(list1))

# s = input("enter a sentence: ")
# l = s.split(" ")
# print(l)
# print(len(l))

# name = input("enter a 2-part name: ")
# r = name.split()
# print("reversed form: ",r[1],r[0])

# print(chr(65))
# print(ord('A'))

# print(1<=1)
# print(1<1)
# print("car"<"cat")
# print("Dog"<"dog")
# # print("fun" in "refunde


# list1 = [6,4,-5,3.5]
# list1.sort()
# # print(list1)
# list2 = ["ha","hi",'B','7']
# list2.sort()
# print(list2)


# str1 = "accc"
# str2 = "acccbbbbaccc"
# print(str2.startswith(str1))
# print(str2.endswith(str1))


# print(chr(104)+chr(105))
# # print('C'+chr(35))
# a =2
# b = 3
# print(3*a == 2*b)



# print("9w" != "9w")
# print(not True)
# print(True and False)
# # print(False and False)
#
#
# answer = eval(input("how many qallons does a ten-gallon hat hold ?"))
# if (0.5<= answer <=1):
#     print("good, ",end=" ")
# else:
#     print("no, ",end=" ")
# print("it holds about 3/4 of a gallon")


# firstnumber = eval(input("enter first number: "))
# secondnumber = eval(input("enter second number: "))
# thirdnumber = eval(input("enter third number: "))
# max = firstnumber
# if secondnumber >max:
#     max = secondnumber
# if thirdnumber >max:
#     max = thirdnumber
# print("the largest number is",str(max) + ".")
#
# '''
# 嵌套 if-else语句
# '''
#
# color = input("enter a color (Blue or Red): ")
# mode = input("enter a mode(STEADY or FLASHING): ")
# color = color.upper()
# mode = mode.upper()
#
# result = ""
# if color == "BLUE":
#     if mode == "STEADY":
#         result = 'clear view'
#     else:
#         result = 'clouds due'
# else:
#     if mode == "STEADY":
#         result = 'rain ahead'
#     else:
#         result = 'snow ahead'
# print("the weather forecast is",result)


'''
计算利润
'''
#
# costs = eval(input("enter total cost: "))
# revenue = eval(input("enter total revenue: "))
# if costs == revenue:
#     result = "break even."
# else:
#     if costs < revenue:
#         profit = revenue - costs
#         result = "profile is ${0:,.2f}.".format(profit)
#     else:
#         loss = costs - revenue
#         result = "loss is ${0:,.2f}".format(loss)
# print(result)

# num1 = input("enter first number: ")
# num2 = input("enter second number: ")
# if num1.isdigit() and num2.isdigit():
#     print("the sum is ",str(eval(num1) + eval(num2)) + ".")
# elif not num1.isdigit():
#     if not num2.isdigit():
#         print("neither entry was a proper number.")
#     else:
#         print("the first entry was not a proper number.")
# else:
#     print("the second entry was not a proper number.")


#
# major = input( "--")
# if major in["business", "computer science"] :
#     print("yes")
# else:
#     print("no")


# bill = eval(input("enter amount of bill: "))
# tip = 0.15*bill
# if tip < 2:
#     print("tip is $2.0")
# else:
#     print("tip is ${0:,.2f}".format(tip))
'''
修改：---
'''
# bill = float(input("enter amount of bill: "))
# tip = 0.15*bill
# if (tip < 2):
#     tip = 2
# print("tip is ${0:,.2f}".format(tip))


# a = input("who was the first ronald mcdonald?")
# if a == "willard scott":
#     print("you are correct")
# else:
#     print("nice try~")

# score = []
# score.append(eval(input("enter first score: ")))
# score.append(eval(input("enter second score: ")))
# score.append(eval(input("enter third score: ")))
# score.remove(min(score))
# average = sum(score)/2
# print("average of the two higest scores is {0:.2f}".format(average))

#
# weight = eval(input("enter weight in ponds: "))
# payment = eval(input("enter payment in dollaes: "))
# pay = weight*2.5
# change = payment - pay
# if change <0:
#     print("you own ${0:.2f}".format(change))
# else:
#     print("your change is ${0:.2f}".format(change))


'''
要求用户输入单个大写字母
'''

# letter = input("enter a single uppercase letter:")
# if (len(letter)!=1) or (letter != letter.upper()):
#     print("you did not comply with the request.")
#


'''
军用时间转换为普通时间
'''

# militaryTime = input("enter a militaryTime (0000 to 2359):")
# hours = int(militaryTime[0:2])
# minutes = int(militaryTime[2:4])
# if hours > 12:
#     cycle = "pm"
#     hours %= 12
# else:
#     cycle = "am"
#     if hours == 0:
#         hours = 12
# print("the regular time is {0}:{1}{2}".format(hours,minutes,cycle))



'''
嵌套的if-else
'''

# gpa = eval(input("enter your gpa: "))
# if gpa > 3.9:
#     honours = "summa cum laude."
# elif gpa >= 3.6:
#     honours = "magna cum laude."
# elif gpa >= 3.3:
#     honours = "cum laude"
# else:
#     honours = "."
# print("your graduated "+ honours)


'''
if
'''

# gpa = eval(input("enter your gpa: "))
# if gpa >= 3.9:
#     honours = "summa cum laude."
# if 3.6 <= gpa <3.9:
#     honours = "magna cum laude."
# if 3.3<= gpa <3.6:
#     honours = "cum laude"
# if gpa <3.3 :
#     honours = "."
# print("your graduated ", honours)


'''
判断所得税：
'''

# taxable = float(input("enter your taxable income: "))
# if taxable <= 20000:
#     tax = 0.02*taxable
# if 20000 < taxable <= 50000:
#     tax = 400+0.025*(taxable-20000)
# if taxable >50000:
#     tax = 1150+0.035*(taxable-50000)
# print("your tax is ${0:.2f}".format(tax))


#
# taxable = float(input("enter your taxable income: "))
# if taxable <= 20000:
#     tax = 0.02*taxable
# elif taxable <= 50000:
#     tax = 400+0.025*(taxable-20000)
# else:
#     # taxable >50000:
#     tax = 1150+0.035*(taxable-50000)
# print("your tax is ${0:.2f}".format(tax))



# taxable = float(input("enter your taxable income: "))
# if taxable <= 20000:
#     tax = 0.02*taxable
# else:
#     if taxable <= 50000:
#         tax = 400+0.025*(taxable-20000)
#     else:
#     # taxable >50000:
#         tax = 1150+0.035*(taxable-50000)
# print("your tax is ${0:.2f}".format(tax))

'''while 循环'''

# num = 1
# while num <= 5:
#     print(num)
#     num += 1
#     print("#",num)
#
#
# print("this program displays a famous moive quotation.")
# responses = ('1','2','3')
# response = '0'
# while response not  in responses:
#     response = input("enter 1 ,2 ,or 3: ")
#     if response == '1':
#         print("plastics.")
#     elif response == '2':
#         print("rosebud")
#     elif response == '3':
#         print("that is all folks.")


# count = 0
# total = 0
# print("(enter -1 to terminate entering numbers,)")
# num = eval(input("enter a nonnegative number: "))
# min = num
# max = num
# while
#
#     count +=1
#     total += num
#     if num < min:
#         min = num
#     if num > max:
#         max = num
#     num = eval(input("enter a nonnegative number : "))
#
# if count >0:
#     print("minimum:",min)
#     print("maximum:",max)
#     print("average: ",total / count)
# else:
#     print("no nonnegative number were entered.")


# list1 =[]
# print("(enter -1 to terminate entering numbers.)")
# num = eval(input("enter a nonnegative number: "))
# while num != -1:
#     list1.append(num)
#     num = eval(input("enter a nonnegative number: "))
#     #display result
# if len(list1) > 0:
#     list1.sort()
#     print("minimum: ",list1[0])
#     print("maximum: ",list1[-1])
#     print("average:",sum(list1) / len(list1))
# else:
#     print("no nonnegative number were entered.")


'''
复合利率
'''
# numberOfYears = 0
# balance = eval(input("enter initial deposit: "))
# while balance < 1000000:
#     balance += .04* balance
#     numberOfYears += 1
# print("in",numberOfYears,"years you will have a million dollars.")


'''
break语句
'''
#
# list1 = []
# print("(enter -1 to terminate entering numbers.)")
# while True:
#     num = eval(input("enter a nonnegative number: "))
#     if num == -1:
#         break
#     list1.append(num)
# print(list1)
#
# list1 = ["one",23,17.5,"two",33,44,55,66,22.1,242,"three"]
# i = 0
# foundFlag = False
# while i < len(list1):
#     x = list1[i]
#
#     i+=1
#
#     if not isinstance(x,int):
#         continue
#     if x % 11 == 0:
#         foundFlag = True
#         print(x,"is the first int that is divisible by 11.")
#         break
# if not foundFlag:
#     print("three is no int in the list that is divisible by 11")

#
# print("enter a number from the menu to obtain a fact")
# print("about the united state or to exit the program.\n")
# print("1.capital")
# print("2.national bird")
# print("3.national flower")
# print("4.quit\n")
# while True:
#     num = int(input("make a selection from the menu: "))
#     if num == 1:
#         print("washington,dc is the capital of the united states.")
#     elif num == 2:
#         print("the american bald eagle is the national bird.")
#     elif num == 3:
#         print("the rose is the national flower.")
#     elif num == 4:
#         break


'''
无限循环
'''

# print("enter -1 to terminate entering numbers.")
# number = 0
# while number >= 0:
#     number = eval(input("enter a number to square: "))
#     number = number * number
#     print(number)
#
#

# total = 0
# print("enter -1 to terminate entering numbers.")
# num = 0
# while num != -1:
#     total += num
#     print(total)
#     num = eval(input("enter a positive number: "))
#     print(num)
#
# print("total: ",total)
#

# while answer.upper() != "SHAZAM":
# answer = input("enter the password: ")
#     print("you may continue")


# while True:
#     answer = input("enter the password: ")
#     if answer.upper() == "SHAZAM":
#         break
# print("you may cotinue")



# sum = 0
# num = 2
# while num < 10:
#     sum += num
#     num += 3
#     print(sum)
#
# list1 = [2,4,6,8]
# total = 0
# while list1:
#     total += list1[0]
#     list1 = list1[1:]
#     print("total: ",total)
#     print("list1: ",list1)
# print(total)

# q = 1
# num = 0
# while q > 0:
#     q = 3 *q -1
#     num += 1
#     if num == 1:
#         print(q)

#
# num = 0
# while True:
# #     num = 1
# #     num += 1
# #     print(num)
#
# list1 = ['a','b','c','d']
# i = -1
# while i <(len(list1) - 1):
#     i += 1
#     print(list1[i])


# for i in range(3):
    # name = input("enter a name: ")
    # print(name)


# f = [2,4,6,8]
# total = 0
# while f != []:
#     total += f[0]
#     print("total",total)
#     f = f[1:]
#     print("f",f)
# print(total)


# print("celsius \t\tfah")
# for celsius in range(10,31,5):
#     fah = ((9/5)*celsius)+32
#     print("{0}\t\t{1:.0f}".format(celsius,fah))


# m = eval(input("enter value of M: "))
# n = eval(input("enter value of N: "))
# while n != 0:
#     t = n
#     print("t",t)
#     n = m%n
#     print("n",n)
#     m = t
#     print("m",m)
#
# # print("gcd: ",m)
#
# age = 1
# while(1980+age) != (age * age):
#     age += 1
# print("person will be {0} \n in the year {1} ".format(age,age*age))


# mass = 100
# year = 0
# while(mass > 1):
#     mass /= 2
#     year += 28
# print("the dency time is ")
# print(year,"years.")
#
#


# principal = 15000
# balance = principal #inatial balance
# monthlyPayment = 290
# monthlyFactor = 1.005
# month = 0
# while(balance >= principal /2):
#     balance = (monthlyFactor*balance) - monthlyPayment
#     month += 1
# print("load will be half paid \noff after",month,"month.")
#
# balance = 10000
# # money2 = money
# m1 = 600
# r = 1.003
# month = 0
# while balance > 600:
#     balance = r*balance - m1
#     month += 1
# print("balance will be ${0:,.2f} ".format(balance))
# print("after",month,"months")

#
# num = 1
# while (364/365) ** num >0.5:
#     num += 1
# print("with",num,"students,the probability...")
# #
#
# chinapop = 1.37
# indiapop = 1.26
# year = 2014
# while indiapop < chinapop:
#     year += 1
#     chinapop *= 1.0051
#     indiapop *= 1.0135
# print(year,"year")
#
#
#
# for i in range(2,6):
#     print(i,i*i)


# pop = 300000
# print("{0:10} {1}".format("year","population"))
# for year in range(2014,2019):
#     print("{0:<10d} {1:d}".format(year,round(pop)))
#     pop += 0.03*pop
#

# initialDeposit = eval(input("enter amount deposited: "))
# prompt = "enter annual rate of interest;such as .02,.03,or .04: "
# annualRateOfInterest = eval(input(prompt))
# monthlyRateOfInterest = annualRateOfInterest / 12
# print("{0}{1:>13}".format("month","balance"))
# for i in range (3,13,3):
#     print("{0:2}       ${1:<17,.2f}".format(i,initialDeposit *(1+monthlyRateOfInterest) ** i))

#
# for m in range (1,10):
#     for n in range(1,10):
#         print(m,'x',n,'=',m*n,"\t",end = "")
#     print()

'''
星号三角形
'''

# numberOfRows = int(input("enter a number from 1 through 20 : "))
# for i in range(numberOfRows):
#     for j in range(i+1):
#         print("*",end="")
#     print()



# for i in range(10):
#     print(" ".join(["%dX%d=%-2d"%(m,i,m*i) for m in range(1,i+1)]))   # %d按照整型格式化输出，-表示左对齐，2表示数字不足2位则补齐两位，不足位置用空格


#
# word = input("enter a word: ")
# reversedWord = ""
# for ch in word:
#     reversedWord = ch + reversedWord
# print("the reversed word is " + reversedWord + ".")


# months = ("j","f","m","a","m")
# from month in  months:
#     if 'r' in months.lower():
#         print(months)

# months = ["j","f","m","a","m","j","ju","au","sep","o","n","de"]
# for i in range(len(months)):
#     months[i] = months[i][0:3]
# print(months)

# ranks = ['2','3','4','5','6','7','8','9','10',"jack","queen","king","ace"]
# suits = ["spades","hearts","clubs","diamonds"]
# deckOfCards = []
# for rank in ranks:
#     for suit in suits:
#         deckOfCards.append(rank + "of "+suit)
# for card in deckOfCards:
#     print(card)
# #
# firstname = input("enter a first name: ")
# foundFlag = False
#
# infile = open('E:\\uspres.txt','r')
# for line in infile:
#     if line.startswith(firstname + ' '):
#         print(line.rstrip())
#         foundFlag = True
# infile.close()
# if not foundFlag:
#     print("no president had the first name",firstname + '.')
#
# infile = open('E:\\uspres.txt','r')
# for line in infile:
#     pass
# print(line.rstrip())
#
# infile.close()


# datalist = []
# infile = open('E:\\uspres.txt','r')
# for line in infile:
#     datalist.append(line.strip())
# infile.close()



# infile = open('E:\\uspres.txt','r')
# datalist = [eval(line) for line in infile]
# infile.close()
#
# musketeers = ["athos","porthos","aramis","d'artagnan"]
# i = 0
# while i < len(musketeers):
#     print(musketeers[i])
#     i+= 1


#
# list1 = [1,2,"three","six",4,5,"seven",8,3.1416]
# for item in list1:
#     if isinstance(item,str):
#         break
#
# for j in range(1,26):
#     print(j)

#
# list1 = [2,5,7,2,7,8]
# list2 = []
# for item in list1:
#     if item not in list2:
#         list2.append(item)
# # print(list2)
#
# for i in range(1,4):
#     # print(type(i))
#     print(i + 2** i)
#
# list1 = ['a','b','c']
# # letter = []
# for letter in list1:
#     # print(letter)
#     letter=letter.upper()
#     print(letter)

#
# for i in range(0,20):
#     if i != 13:
#         print(i)

# list1 = ["one","two","three","four"]
# for item in list1:
#     item = item.upper()
#     print(item)

# num = 1
# while num <= 9:
#     print(num)
#     num+=2
#

# for num in range(1,10,2):
#     print(num)

# print("hello")
# print("hello")
# print("hello")
# print("hello")
#
# for i in range(4):
#     print("hello")


# lakes = ["eric","huron","michigan","ontario","superior"]
# result = ""
# for i in range(len(lakes)):
#     result += lakes[i]
#     if i < len(lakes) - 1:
#         result += ","
# print(result)
#
# lakes = ["eric","huron","michigan","ontario","superior"]
# for result in lakes:
#     print(result)

#
# lakes = ["eric","huron","michigan","ontario","superior"]
# print(",".join(lakes))



# lakes = ["eric","huron","michigan","ontario","superior"]
# for i in range(len(lakes)):
#     print(lakes[i],end="")
#     if i < len(lakes) - 1:
#         print("|",end="")


# lakes = ["eric","huron","michigan","ontario","superior"]
# print("|".join(lakes))


# amount = 10
# for i in range(5):
#     print(i)
#     amount *= .88
# print("is {0:.2f} grams".format(amount) )


# number = input("number is : ")
# # wd = number[0:3]+number[4:7]+number[8:12]
# # print(wd)



# phrase = input("enter the prase: ")
# num = 0
# for i in phrase:
#     if i in["i","e","a","o","u"]:
#         num+=1
#     print(num)


# total = 0
# phrase = input(" enter a phrase: ")
# phrase.lower()
# for ch in phrase:
#     if ch in "aeiou":
#         total+=1
# print( "count is: ",total)

# a = eval(input("enter the 1 number: "))
# b = eval(input("enter the 2 number: "))
# c = eval(input("enter the 3 number: "))
# max = a
# if b > max:
#     max = b
# if c > max:
#     max = c
# print("the largest number is : ",max)


# print("the sum 1+1/2 + 1/3 + 1/4 + ...+1/100 is ")
# sum = (1+1/100)*100/2
# print(sum)
# print("to five decimal places")

# sum = 0
# for i in range(1,101):
#     sum += 1/i
# print("sum = {0:.5f} to five.....".format(sum))

#
#
# sum = 0
# for i in range(101):
#     sum += i
# print(sum)

#
# word = input("enter a word: ")
# firstletetr = ""
# secondletter = ""
# sss = True
# for i in range(0,len(word)-1):
#     firstletetr = word[i]
#     print("diyi",firstletetr)
#     secondletter = word[i+1]
#     print("dier",secondletter)
#     if firstletetr >secondletter:
#         sss = False
#         break
# if sss\
#
#         :
#     print("in order")
# else:
#     print("not in order")
#
# # print('a'>'b')
# print('a'<'b')



# input("enter name: ")
# age = int(input("enter age: "))
# salary = float(input("enter starting salary: "))
# earn = 0
#
# for i in range(age,65):
#     earn += salary
#     salary += .05*salary
# print("earn: ${0:,.0f} ".format(earn))

#
# r = 0.05
# salary = int(input("salary: "))
# print("simple interest  ","compound interest")
# for year in range(1,5):
#     earn = salary*r*year
#     money = salary+earn
#     mon = salary*(1+0.05)**year
#     print("{0}.${1} \t\t\t\t{2}".format(year,money,mon))
#


# print("          amount owen at")
# print("year    ","end of year")
#
# balance = 15000
# year = 2012
# for year in range(1,49):
#     balance = (1.005*balance) - 290
#     if i % 12 == 0:
#         year += 1
#
#         print(year, "  ${0:,.2f}".format(balance))
# print(year+1," $0.00")
#
# nums = []
# for i in range (3):
#     num = int(input("enter a grade : "))
#     nums.append(num)
# nums.sort()
# average = (nums[1]+nums[2])/2
# print(average)
#

# datas = []
# count = int(input("enter the count you want calculate: "))
# for i in range (count):
#     data = int(input("enter a number: "))
#     datas.append(data)
# datas.sort()
# L=len(datas)
# m=L//2
# if L%2 == 0:
#     media =(datas[m]+datas[m-1])/2
# else:
#     media =datas[m]
# print(media)


# salary = 20000
# optionl = 0
# # for i in range(10):
# #     optionl += salary
# #     salary += 1000
# # print("option 1 earn ${0:,d}".format(optionl))
# salary = 1000
# option2 = 0
# for i in range(20):
#     option2  += salary
#     salary += 250
# print("option 2 earn ${0:,d}".format(option2))


#
# word = input("enter a word: ")
# word = word.upper()
# vowels = "AEIOU"
# vowelsFound = []
# numVowels = 0
# # print("#",vowelsFound)
# for letter in word:
#     if (letter in vowels) and (letter not in vowelsFound):
#         numVowels += 1
#         vowelsFound.append(letter)
#         print(vowelsFound)
# # print("number of vowels: ",numVowels)



# for r in range(21,26):
#     product = 1
#     for t in range(1,r):
#         product=product*((365-t)/365)
#     print("{0}   {1:.3f}".format(r,1-product))


#p118 t76
# infile = open('E:\\state.txt','r')
# listname = [line.rstrip() for line in infile]
# listname.sort()
# print(listname)


# sentence = input("enter a sentence: ")
# newSentence = ""
# for ch in sentence:
#     if ch.upper() != 'R':
#         newSentence += ch
# print(newSentence)
#

# infile = open('E:\\uspres.txt','r')
# for i in range(15):
#     infile.readline()
# print("the 16th president was")
# print(infile.readline().rstrip()+'.')

# theString = 'saaaay yes no yaaaass'
# a= theString.strip('say')
# b= theString.strip('say ') #say后面有空格
# c= theString.lstrip('say')
# d= theString.rstrip('say')
# print("a:",a,"b:",b,"c:",c,"d:",d)


# total = 0
# for n in range(1000000):
#     if '1' in str(n):
#         total+=1
# print("{0:,d} number on the odometer".format(total))
# print("contain the digit1")





# justices = ["scalia r","kennedy r","thomas r","finsburg d","beryer d","roberts r","alito r","sotomayor d","kagan d"]
# demappointtees = []
# repappointees = []
# for justice in justices:
#     if justice[-1] =='d':
#         demappointtees.append(justice[:-2])
#     else:
#         repappointees.append(justice[:-2])
# named = ','.join(demappointtees)
# namer = ','.join(repappointees)
# print("demappointtees: ",named)
# print("repappointees: ",namer)
# #
# #
# def fahrenheiToCelsius(t):
#     convertedTemperature = (5/9)*(t-32)
#     return convertedTemperature
# fahrenheiTemp = eval(input("enter a temperature in degree Fahrenheit: "))
# # celsiusTemp = fahrenheiToCelsius(fahrenheiTemp)
# # print("celsius equivalent:",celsiusTemp,"degrees")
#
# print("celsius equivalent:" ,fahrenheiToCelsius(fahrenheiTemp),"degrees")



#
# def firstName(fullName):
#     firstSpace = fullName.index(" ")
#     print(firstSpace)
#     givenName = fullName[:firstSpace]
#     return givenName
# fullName = input("enter a person's full name: ")
# print("first name:",firstName(fullName))
#
# def triple(num):
#     num = 3*num
#     return num
# def triple(num):
#     product = 3*num
#     return product
# num = 2
# print(triple(num))
# print(product)


# def pay(wage,hours):
#     if hours <= 40:
#         amount = wage * hours
#     else:
#         amount = (wage *40) + ((1.5) *wage * (hours - 40))
#     return amount
# # def futureValue(p,r,m,t):
# #     i = r/m
# #     n = m*t
# #     amount = p *((1+i) ** n)
# #     return amount
# houryWage = eval(input("enter the hourly wage: "))
# hoursworked = eval(input("enter the number of hours worked: "))
# earnings = pay(houryWage,hoursworked)
# print("earning: ${0:,.2f}".format(earnings))


# def futureValue(p,r,m,t):
#     i = r/m
#     n = m*t
#     amount = p*((1+i) **n)
#     return amount
# p = eval(input("enter amount deposited: "))
# r = eval(input("enter annual rate of interest in decimal form: "))
# m = eval(input("enter number of times interest is compounded per years: "))
# t = int(input("enter number of years: "))
# balance = futureValue(p,r,m,t)
# print("balance after",t,"years: ${0:,.2f}".format(balance))



# def isVowelWord(word):
#     word = word.upper()
#     vowels = ('A','E','I','O','U')
#     for vowel in vowels:
#         if vowel not in vowels:
#             return False
#     return True
# word = input('enter a word: ')
# if isVowelWord(word):
#     print(word,'contain every vowel.')
# else:
#     print(word,'does not contain every vowel')
#

# def oldMcDonald(animal,sound):
#     print("Old Mcdonald had a farm. eyi eyi oh.")
#     print("and on his farm he had a "+ '.',"eyi eyi oh")
#     print("with a ",sound,sound ,"here , and a",sound,sound,"there."
#                                                             ""
#                                                             "")
#     print("here a ",sound,sound + ".",
#           "everywhere a ",sound,sound + ".")
#     print("ord mcdonald had a farm. eyi eyi oh.")
#
# oldMcDonald("lamb","baa")
# print()
# oldMcDonald("duck","quack")
# print()
# oldMcDonald("cow","moo")
# print()

# def main():
#     fullName = input("enter a person's full name: ")
#     print("first name: ",firstName(fullName))
# def firstName(fullName):
#     firstSpace = fullName.index(" ")
#     givenName = fullName[:firstSpace]
#     return givenName
#
# main()

# def main():
#     describeTask()
#     calculateDensity("hawaii",1375000,6423)
# def describeTask():
#     print("this program displays the population")
#     print("density of the last state to become")
#     print("part of the united state.\n")
# def calculateDensity(state,pop,landArea):
#     density = pop/landArea
#     print("the density of",state,"is")
#     print("{0:,.2f} people per square mile.".format(density))
# main()

#
# def main():
#     x = 2
#     print(str(x) + ": function main 1")
#     trivial()
#     print(str(x) + ": function main 2")
# def trivial():
#     x =3
#     print(str(x) + ": function trivial 3")
# main()

# def main():
#     x =5
#     # trivial()
#     # print(x ,"$")
# def trivial():
#     x = 6
#     print(x)
# trivial()

# x = 0
# def main():
#     print(str(x) + ":function main 1")
#     trivial()
#     print(str(x) + ":function main 2")
# def trivial():
#     global x
#     x += 7
#     print(str(x) + ":function main 3")
# main()
# INTEREST_RATE = 0.04
# MINIMUM_VOTING_AGE = 18
# BOOK_TITLE = "progrimming with python"
# amountDeposoted = 5
# age = int(input("input age"))
# interestEarned = INTEREST_RATE * amountDeposoted
# if (age >= MINIMUM_VOTING_AGE):
#     print("you are eligible to vote.")
# print("the title of the book is ",BOOK_TITLE +".")





# hourlyWage = eval(input("enter the hourly wage: "))
# hoursworked = eval(input("enter the number of hours worked: "))
# earnings = finance.pay(hourlyWage,hoursworked)
# print("earnings : ${0:,.2f}".format(earnings))


# import finance

#
#
# r = eval(input("enter annual rate of interest in decimal form: "))
# m = eval(input("enter number of times interest is compounded per years: "))
# t = int(input("enter number of years: "))
# balance = futureValue(p,r,m,t)
# print("balance after",t,"years: ${0:,.2f}".format(balance))

# coding=utf-8
# import turtle
# import time
#
# # 同时设置pencolor=color1, fillcolor=color2
# turtle.color("red", "yellow")
#
# turtle.begin_fill()
# for _ in range(50):
#     turtle.forward(200)
# turtle.left(170)
# turtle.end_fill()
#
# turtle.mainloop()


# # coding=utf-8
# import turtle
# import time
#
# turtle.pensize(5)
# turtle.pencolor("yellow")
# turtle.fillcolor("red")
#
# turtle.begin_fill()
# for _ in range(5):
#     turtle.forward(200)
#     turtle.right(144)
# turtle.end_fill()
# time.sleep(2)
#
# turtle.penup()
# turtle.goto(-150, -120)
# turtle.color("violet")
# turtle.write("嘻嘻", font=('Arial', 40, 'normal'))
#
# turtle.mainloop()


# coding=utf-8

# import turtle
# from datetime import *
#
#
# # 抬起画笔，向前运动一段距离放下
# def Skip(step):
#     turtle.penup()
#     turtle.forward(step)
#     turtle.pendown()
#
#
# def mkHand(name, length):
#     # 注册Turtle形状，建立表针Turtle
#     turtle.reset()
#     Skip(-length * 0.1)
#     # 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
#     turtle.begin_poly()
#     turtle.forward(length * 1.1)
#     # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
#     turtle.end_poly()
#     # 返回最后记录的多边形。
#     handForm = turtle.get_poly()
#     turtle.register_shape(name, handForm)
#
#
# def Init():
#     global secHand, minHand, hurHand, printer
#     # 重置Turtle指向北
#     turtle.mode("logo")
#     # 建立三个表针Turtle并初始化
#     mkHand("secHand", 135)
#     mkHand("minHand", 125)
#     mkHand("hurHand", 90)
#     secHand = turtle.Turtle()
#     secHand.shape("secHand")
#     minHand = turtle.Turtle()
#     minHand.shape("minHand")
#     hurHand = turtle.Turtle()
#     hurHand.shape("hurHand")
#
#     for hand in secHand, minHand, hurHand:
#         hand.shapesize(1, 1, 3)
#         hand.speed(0)
#
#     # 建立输出文字Turtle
#     printer = turtle.Turtle()
#     # 隐藏画笔的turtle形状
#     printer.hideturtle()
#     printer.penup()
#
#
# def SetupClock(radius):
#     # 建立表的外框
#     turtle.reset()
#     turtle.pensize(7)
#     for i in range(60):
#         Skip(radius)
#         if i % 5 == 0:
#             turtle.forward(20)
#             Skip(-radius - 20)
#
#             Skip(radius + 20)
#             if i == 0:
#                 turtle.write(int(12), align="center", font=("Courier", 14, "bold"))
#             elif i == 30:
#                 Skip(25)
#                 turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
#                 Skip(-25)
#             elif (i == 25 or i == 35):
#                 Skip(20)
#                 turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
#                 Skip(-20)
#             else:
#                 turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
#             Skip(-radius - 20)
#         else:
#             turtle.dot(5)
#             Skip(-radius)
#         turtle.right(6)
#
#
# def Week(t):
#     week = ["星期一", "星期二", "星期三",
#             "星期四", "星期五", "星期六", "星期日"]
#     return week[t.weekday()]
#
#
# def Date(t):
#     y = t.year
#     m = t.month
#     d = t.day
#     return "%s %d%d" % (y, m, d)
#
#
# def Tick():
#     # 绘制表针的动态显示
#     t = datetime.today()
#     second = t.second + t.microsecond * 0.000001
#     minute = t.minute + second / 60.0
#     hour = t.hour + minute / 60.0
#     secHand.setheading(6 * second)
#     minHand.setheading(6 * minute)
#     hurHand.setheading(30 * hour)
#
#     turtle.tracer(False)
#     printer.forward(65)
#     printer.write(Week(t), align="center",
#                   font=("Courier", 14, "bold"))
#     printer.back(130)
#     printer.write(Date(t), align="center",
#                   font=("Courier", 14, "bold"))
#     printer.home()
#     turtle.tracer(True)
#
#     # 100ms后继续调用tick
#     turtle.ontimer(Tick, 100)
#
#
# def main():
#     # 打开/关闭龟动画，并为更新图纸设置延迟。
#     turtle.tracer(False)
#     Init()
#     SetupClock(160)
#     turtle.tracer(True)
#     Tick()
#     turtle.mainloop()
#
#
# if __name__ == "__main__":
#     main()


#
#
# x = 7
# def main():
#     global x
#     x+=1
#     print(x)
# main()

# def f(x):
#     return (x>0)

#
# def f(x):
#     if x >0:
#         return True
#     else:
#         return False


# def main():
#     print(uc('t'))
#     print(uc('t'))
# def uc(letter):
#     if letter == 'h':
#         return 'H'
#     else:
#         return letter
# main()
#
# name = "Fred"
# def main():
#     global name
#     otherName = getName()
#     name += otherName
#     print(name)
# def getName():
#     name = "rick"
#     return name
# main()


#
# def maximum(list1):
#     largestNumber = list1[0]
#     for number in list1:
#         if number > largestNumber:
#             largestNumber = number
#     return largestNumber




#
# def calculate_character_num(s):
#     '''This function calculate each character(from A-z) number from str.'''
#     # 去除字符串中的空格
#     s =list( ''.join(s.split()))
#     # 去重
#     s1 = set(s)
#     # 转换成列
#     l = list(s1)
#     t ={}
#
#     for a in range(len(l)):
#         num = 0
#         for i in reversed(range(len(s))):
#             if l[a] == s[i]:
#                 num = num + 1
#                 s.pop(i)
#         t[l[a]] = str(num)
#     return t
#
# if __name__ == '__main__':
#     str1 = 'hello world'
#     t = calculate_character_num(str1)
#     print(t)







# str=input("请输入一个字符串:")
# res={}
# for i in str:
#     if  i  in res:
#         res[i]=res[i]+1
#     else:
#         res[i]=1
# print(res)

# def main():
#     word = input("enter a word; ")
#     if isQwerty(word):
#         print(word,"is a qwerty word")
#     else:
#         print(word,"is not a qwerty word")
# def isQwerty(word):
#     word = word.upper()
#     for ch in word:
#         if ch not in "QWERTYUIOP":
#             return False
#     return True
# main()

# def main():
#     num = int(input("enter a number"))
#     print( num,"!"," is ",number(num))
# def number(num):
#     if num == 0 or num == 1:
#         return 1
#     total = 1
#     for i in range(2, num + 1):
#         total *= i
#     return total
# main()


# def main():
#     opt1 = option1()
#     opt2 = option2()
#     print("option 1 = ${0:,.2f}".format(opt1))
#     print("option 2 = ${0:,.2f}".format(opt2))
#
#     if opt1 > opt2:
#         print("option1 is better")
#     elif opt1 == opt2:
#         print("both ok")
#     else:
#         print("option 2 is better")
# def option1():
#     sum = 0
#     for i in range(10):
#         sum += 100
#     return sum
# def option2():
#
#     sum = 0
#     daySalary = 1
#     for i in range(10):
#         sum += daySalary
#         daySalary *= 2
#     return sum
# main()


# def main():
#     f = input("enter first name:")
#     s = input("enter last name: ")
#     global salary
#     salary = int(input("enter current salary: "))
#
#     print("new salary for ",f,s,":",sal())
# def sal():
#     if salary <40000:
#         total = salary*1.05
#     else:
#         if salary >= 40000:
#             total = (salary-40000)*0.02 + salary + 2000
#     return total
# main()
#
# WAGE_BASE = 117000
# SOCIAL_SECURITY_TAX_PATE = 0.062
# MEDICARE_TAX_RATE = 0.0145
# ADDITIONAL_MEDICARE_TAX_RATE = .009
# def main():
#     ytdEarnings,curEarnings,totalEarnings = obtainEarnings()
#     socialSecurityBenTax = calculateBenTax(ytdEarnings,curEarnings,totalEarnings)
#     calculateFICAtax(ytdEarnings,curEarnings,totalEarnings,socialSecurityBenTax)
# def obtainEarnings():
#     str1 = "enter total earnings for this year...:"
#     ytdEarnings = eval(input(str1))
#     curEarnings = eval(input("enter earnings for the current pay period: "))
#     totalEarnings = ytdEarnings + curEarnings
#     return (ytdEarnings,curEarnings,totalEarnings)
# def calculateBenTax(ytdEarnings,curEarnings,totalEarnings):
#     socialSecurityBenTax = 0
#     if totalEarnings < WAGE_BASE:
#         socialSecurityBenTax = SOCIAL_SECURITY_TAX_PATE *curEarnings
#     elif ytdEarnings < WAGE_BASE:
#         socialSecurityBenTax = SOCIAL_SECURITY_TAX_PATE * (WAGE_BASE  -ytdEarnings)
#     return socialSecurityBenTax
# def calculateFICAtax(ytdEarnings,curEarnings,totalEarnings,socialSecurityBenTax):
#     medicareTax = MEDICARE_TAX_RATE * curEarnings
#     if ytdEarnings >= 200000:
#         medicareTax += ADDITIONAL_MEDICARE_TAX_RATE * curEarnings
#     elif totalEarnings > 200000:
#         medicareTax += ADDITIONAL_MEDICARE_TAX_RATE * (totalEarnings - 200000)
#     ficaTax = socialSecurityBenTax + medicareTax
#     print("FICA tax for the current pay period :${0:,.2f}".format(ficaTax))
# main()


# def main():
#     firstPart()
#     print(str(4) + ":from function main")
# def firstPart():
#     print(str(1) + ":from function firstPart")
#     secondPart()
#     print(str(3) + ":from function firstPart")
# def secondPart():
#     print(str(2) + ":from function firstPart")
# main()


# INTEREST_RATE = 0.04  #annual rate of interest
# def main():
#     principal = eval(input("enter the amount of the deposit: "))
#     numberOfYears = eval(input("enter the number of years: "))
#     (bal,intEarned) = balanceAndInterest(principal,numberOfYears)
#     print("Balance: ${0:,.2f}     Interest Earned :${1:,.2f}".format(bal,intEarned))
# def balanceAndInterest(prin,numYears):
#     balance = prin * ((1 + INTEREST_RATE) ** numYears)
#     interestEarned = balance - prin
#     return (balance,interestEarned)
# main()


# INTEREST_RATE = 0.04
# def main():
#     (principal,numberOfYears) = getInput()
#     bal,intEarned = balanceAndInterest(principal,numberOfYears)
#     displayOutput(bal,intEarned)
# def getInput():
#     principal = eval(input("enter the amount of the deposit: "))
#     numberOfYears = eval(input("enter the number of years: "))
#     return (principal,numberOfYears)
# def balanceAndInterest(prin,numYears):
#     balance = prin * ((1 + INTEREST_RATE) ** numYears)
#     interestEarned = balance - prin
#     return (balance,interestEarned)
# def displayOutput(bal,intEarned):
#     print("Balance:${0:,.2f}      Interest Earned :${1:,.2f}".format(bal,intEarned))
# main()

# f(x)=[]
# list1 = ['2','3','6','7']
# list2 = [f(x) for x in list1]
# # list1 = ['2','3','6','7']


# def total(w,x,y=10,z=20):
#   return (w**x)+y+z
# print(total(2,y=4,x=3))
# # # def num(a,b):
# #     a=2
# #     b=3
#     return (a,b)
#
# def main():
#     q = "what is the capital of California?"
#     a = "Sacramento"
#     askQuestion(q,a)
# def askQuestion(question,answer,numberOfTries = 3):
#     numTries = 0
#     while numTries < numberOfTries:
#         numTries += 1
#         ans = input(question)
#         if ans == answer:
#             print("correct!")
#             break
#     if ans != answer:
#             print("you have esed up your allotment of guesses.")
#             print("the correct answer is ",answer +'.')
# main()

# def main():
#     print("balance: ")
#     print("${0:,.2f}".format(balance(1000,5)))
#     print("${0:,.2f}".format(balance(1000,5,.04)))
#     print("${0:,.2f}".format(balance(1000,intRate=.04,numYears = 5)))
#     print("${0:,.2f}".format(balance(numYears = 5,prin=1000)))
#     print()
#     print("balance: ")
#     print("${0:,.2f}".format(balance(1000, 5,.03)))
#     print("${0:,.2f}".format(balance(1000, intRate = .03,numYears = 5)))
#     print("${0:,.2f}".format(balance(intRate = .03, numYears = 5, prin=1000)))
#     print("${0:,.2f}".format(balance(numYears=5,intRate = .03,prin=1000)))
# def balance(prin,numYears,intRate = .04):
#     return prin *((1+intRate) ** numYears)
# main()


# def main():
#     list1 = ["democratic","sequoia","equals","brrr","break","two"]
#     list1.sort(key=len)
#     print("sorted by length in ascending order: ")
#     print(list1,'\n')
#     # list1.sort(key=lastCharacter)
#     list1.sort(key=lambda x:x[-1])
#     print("sorted by last character in ascending order; ")
#     print(list1,'\n')
#     list1.sort(key=numberOfVowels,reverse = True)
#     print("sorted by number of vowels in descending order: ")
#     maxValue = max(list1,key=numberOfVowels)
#     minValue = min(list1,key= numberOfVowels)
#     print(list1)
#     print(maxValue)
#     print(minValue)
# # def lastCharacter(word):
# #     return word[-1]
# def numberOfVowels(word):
#     vowels = ('a','e','i','o','u')
#     total = 0
#     for vowel in vowels:
#         total += word.count(vowel)
#     return total
# main()
#
#
# names = ["dennis ritchie","alan kay","john backus","james gosling"]
# names.sort(key = lambda name: name.split()[-1])
# # nameString = ",".join(names)
# print(names)



# list1 = ["white","blue","red"]
# list2 = sorted(list1)
# list3 = sorted(list1,reverse=True)   #进行反向排序
# list4 = sorted(list1,key=len)
# list5 = sorted("spam")
# print("2: ",list2)
# print("3: ",list3)
# print("4: ",list4)
# print("5: ",list5)




#
# list1 = ['c','D','a','B']
# print(sorted(list1))
# print(sorted(list1,key=lambda letter:letter.upper()))



#
# def main():
#     howMany(24)
#     print("a pie.")
# def howMany(num):
#     what(num)
#     print("baked in",end=" ")
# def what(num):
#     print(num,"blackbirds",end=" ")
# main()

#
# def main():
#     n,yob = getNameAndYOB()
#     print(n,"will be",2020-yob,"years old in 2020.")
# def getNameAndYOB():
#     name = input("enter a name: ")
#     yearOfBirth = int(input("enter a year of birth: "))
#     return name,yearOfBirth
# main()



# def main():
#     weight = float(input("enter the number of ounces: "))
#     print("cost:${0:0,.2f}".format(cost(weight)))
# def cost(weight):
#     return 0.05+0.1*ceil(weight -1)
# def ceil(x):
#     if int(x) != x:
#         return int(x + 1)
#     else:
#         return x
# main()

#
# def main():
#     word1 = input("enter the first word or pharse: ")
#     word2 = input("enter the second word or pharse: ")
#     if areAnagrams(word1,word2):
#         print("Are anagrams")
#     else:
#         print("Are not anagrams")
# def areAnagrams(word1,word2):
#     firstString = word1.lower()
#     secondString = word2.lower()
#     #字符串的遍历？？
#     letters1 = [ch for ch in firstString if 'a' <= ch <= 'z']
#     letters2 = [ch for ch in secondString if 'a' <= ch <= 'z']
#     letters1.sort()
#     letters2.sort()
#     #注意返回值，返回单词1 == 单词2
#     return (letters1 == letters2)
# main()

# a = eval(input("enter grade 1: "))
# b = eval(input("enter grade 2: "))
# c = eval(input("enter grade 3: "))
# d = eval(input("enter grade 4: "))
# e = eval(input("enter grade 5: "))
# num=[]
# num.append(a)
# num.append(b)
# num.append(c)
# num.append(d)
# num.append(e)
# num.sort()
# # print(num)
# print("range: ",num[4] - num[2])
# print("average: ",(num[2]+num[3]+num[4]) / 3)
# # def main():
# #     print("range: ",range)
# #     print("Average: ",average)
# # def range():
# #     return  (num[4] - num[2])
# #
# # def average():
# #     return (num[2]+num[3]+num[4]) / 3
# # main()



# def main():
#     pres = [("johnson","lyndon"),("john","kennedy"),("andrew","johnson")]
#     pres.sort(key=lambda person:person[0])
#     pres.sort(key=lambda person:person[1])
#     for person in pres:
#         print(person[1] + ',',person[0])
# main()




#人口降序
# def main():
#     NE = [("Maine",30840,1.329),("vermont",9217,.626),("New Hampshire",8953,1.321),("Massachusetts",7800,6.646),("Connecticut",4842,3.59),("Rhode Island",1044,1.05)]
#     NE.sort(key=lambda person:person[2] ,reverse = True)
#     print("sorted by population in descending order: ")
#     for person in NE:
#         print(person[0]," ",end=" ")
#     print()
# main()



#土地面积降序
# def main():
#     NE = [("Maine",30840,1.329),("vermont",9217,.626),("New Hampshire",8953,1.321),("Massachusetts",7800,6.646),("Connecticut",4842,3.59),("Rhode Island",1044,1.05)]
#     NE.sort(key=lambda state:state[1] ,reverse = True)
#     print("sorted by land area in descending order: ")
#     for state in NE:
#         print(state[0]," ",end=" ")
#     print()
# main()


# def main():
#     NE = [("Maine",30840,1.329),("vermont",9217,.626),("New Hampshire",8953,1.321),("Massachusetts",7800,6.646),("Connecticut",4842,3.59),("Rhode Island",1044,1.05)]
#     NE.sort(key=sortByPopulationDensity)
#     print("sorted by length of name in descending order: ")
#     for state in NE:
#         print(state[0]," ",end=" ")
#     print()
# def sortByPopulationDensity(tt):
#     return tt[2] / tt[1]
#
# main()


# def main():
#     numbers = [865,1169,1208,1243,329]
#     numbers.sort(key=largestPrimeFactor)
#     print("sorted by largest prime factor: ")
#     print(numbers)
# def largestPrimeFactor(num):
#     n = num
#     f = 2
#     max = 1
#     while n > 1:
#         if n%f == 0:
#             n = int(n/f)
#             print("n: ",n)
#             if f>max:
#                 max = f
#                 print("max: ",max)
#         else:
#             f += 1
#     return max
# main()



# def main():
#     numbers = [865,1169,1208,1243,329]
#     numbers.sort(key=sumOfDigit)
#     print("sorted by sum of digit: ")
#     print(numbers)
# def sumOfDigit(b1,b2,b3,b4):



# P158 T58:
##待修改

# numbers = [865,1169,1208,1243,329]
# def main():
#     numbers = [865,1169,1208,1243,329]
#     numbers.sort(key=sumOfDigit)
#     print("sorted by sum of digit: ")
#     print(numbers)
#
# def sumOfDigit(i):
#         a1 = i % 10
#         a2 = (i / 10) % 10
#         a3 = (i / 100) % 10
#         a4 = (i / 1000) % 10
#         if len(str(i)) >3:
#             summ = a1+a2+a3+a4
#         else:
#             if len(str(i)) <= 3:
#                 summ = a1+a2+a3
#                 return summ
# main()

# def i():
#     numbers = [865, 1169, 1208, 1243, 329]
#     for i in numbers:
#         return i

# def main():
#     what = "computer"
#     alter(what)
#     print(what)
#
# def alter(what):
#     what = 'typewriter'
# main()
#





# def main():
#     infile = open("E:\\uspres.txt",'r')
#     listPres = [pres.rstrip() for pres in infile]
#     infile.close()
#     listPres.sort(key = sortByLength)
#     for i in range(6):
#         print(listPres[i])
# def sortByLength(pres):
#     return len(pres.split()[0])
# main()
# (x,y) = (2,3)
# def main():
#     z = 5
#     global y
#     y += 1
#     display()
#     print('x:',x,'y:',y,'z',z)
# def display():
#     print(x,y,end=" ")
#     z = 8
# main()


# array = [865, 1169, 1208, 1243, 329]
# # 定义取和
# def a_sun(number):
#     t1 = number % 10
#     l1 = number // 10
#     t2 = l1 % 10
#     l2 = l1 // 10
#     t3 = l2 % 10
#     l3 = l2 // 10
#     t4 = l3 % 10
#     asum = t1 + t2 + t3 + t4
#     return asum
# def a_des(array):
#     for d in range(0, len(array)):
#         for i in range(0, len(array)):
#             if a_sun(array[i]) > a_sun(array[d]):
#
#
#                 array[d], array[i] = array[i], array[d]
# a_des(array)
# print(array)
# # #
#
# def main():
#     file = "E:\\uspres.txt"
#     displayWithForLoop(file)
#     print()
#     displayWithListComprehension(file)
# def displayWithForLoop(file):
#     infile = open(file,'r')
#     for line in infile:
#         print("line:",line,end="")
#     infile.close()
# def displayWithListComprehension(file):
#     infile = open(file,'r')
#     listPres = [line.rstrip() for line in infile]
#     infile.close()
#     print("listPres:",listPres)
# main()


# def main():
#     outfile = open("E:\\uspres.txt",'w')
#     createWithWritelines(outfile)
#     outfile = open("E:\\uspres1.txt",'w')
#     createWithWrite(outfile)
# def createWithWritelines(outfile):
#     list1 = ["a. George Washington","b. John Adams","c . Thomas Jefferson"]
#     for i in range(len(list1)):
#         list1[i] = list1[i] +"\n"
#     outfile.writelines(list1)
#     outfile.close()
# def createWithWrite(outfile):
#         outfile.write("1George Washington\n")
#         outfile.write("2 John Adams\n")
#         outfile.write("3 Thomas Jefferson\n")
#         outfile.close()
# main()


# def main():
#     stateList = createListFormFile("E:\\states.txt")
#     createSortedFile(stateList,"E:\\statesalpha.txt")
# def createListFormFile(filename):
#     infile = open(filename,'r')
#     desiredList = [line.rstrip() for line in infile]
#     infile.close()
#     return desiredList
#
# def createSortedFile(listname,filename):
#     listname.sort()
#     for i in range(len(listname)):
#         listname[i] = listname[i]+"\n"
#     outfile = open(filename,'w')
#     outfile.writelines(listname)
#     outfile.close()
# main()


# def main():
#     vicePresList= createListFromFile("E:\\vpstates.txt")
#     createNewFile(vicePresList,"E:\\states.txt","E:\\both.txt")
# def createListFromFile(fileName):
#     infile = open(fileName,'r')
#     desiredList = [line.rstrip() for line in infile]
#     infile.close()
#     return desiredList
# def createNewFile(listName,oldFileName,newFileName):
#     infile = open(oldFileName,'r')
#     outfile = open(newFileName,'w')
#     for person in infile:
#         if person.rstrip() in listName:
#             outfile.write(person)
#         infile.close()
#         outfile.close()
# main()

#
# def main():
#     outfile = open("E:\\FilrstPresidents.txt",'a')
#     list1 = ["James Madison\n","James Monroe\n"]
#     outfile.writelines(list1)
#     outfile.write("John Q.Adams\n")
#     outfile.close()
# main()

# words = {"spam","ni"}
# # words.clear()
# print(words)
# words.add("eggs")
# print(words)
# words.discard("ni")
# print(words)

# print(set[3,7,3])
# def main():
#     words = ["nudge","nudge","wink","wink"]
#     terms = set(words)
#     print(terms)
#     words = list(terms)
#     print(words)
#     terms.add("nudge")
#     terms.add("maybe")
#     print(terms)
#     terms.discard("nudge")
#     print(terms)
#     words = tuple(terms)
#     print(words)
# main()
#
# a = {x *x for x in range (-3,3)}
# b = list(a)
# b.sort()
# c = set(b)
# print(c)


# def main():
#     infile = open("F:\\file1.txt",'r')
#     firstSet = {line.rstrip() + "\n" for line in infile}
#     infile.close()
#     infile = open("F:\\file2.txt",'r')
#     secondSet = {line.rstrip() + "\n" for line in infile}
#     infile.close()
#     outfile = open("F:\\union.txt",'w')
#     outfile.writelines(firstSet.union(secondSet))
#     outfile.close()
#     outfile = open("F:\\interesection.txt",'w')
#     outfile.writelines(firstSet.intersection(secondSet))
#     outfile.close()
#     outfile = open("F:\\difference.txt",'w')
#     outfile.writelines(firstSet.difference(secondSet))
#     outfile.close()




# def main():
#     vicePresSet = createSetFromFile("F:\\file\\VPres.txt")
#     presSet = createSetFromFile("F:\\file\\USPres.txt")
#     bothPresAndVPresSet = createIntersection(vicePresSet,presSet)
#     writeNamesToFile(bothPresAndVPresSet,"F:\\file\\presAndVPres.txt")
# def createSetFromFile(fileName):
#     infile = open(fileName,'r')
#     namesSet = {name for name in infile}
#     infile.close()
#     return namesSet
# def createIntersection(set1,set2):
#     return set1.intersection(set2)
# def writeNamesToFile(setName,fileName):
#     outfile = open(fileName,'w')
#     outfile.writelines(setName)
#     outfile.close()
# main()


# def main():
#     setOfNewColors = getSetOfNewColors()
#     createFileOfNewColors(setOfNewColors)
# def getSetOfNewColors():
#     infile = open("F:\\file\\pre1990.txt",'r')
#     colors = {line.rstrip() for line in infile}
#     infile.close()
#     infile = open("F:\\file\\retired.txt",'r')
#     retiredColors = {line.rstrip() for line in infile}
#     infile.close()
#     infile = open("F:\\file\\added.txt",'r')
#     addedColors = {line.rstrip() for line in infile}
#     infile.close()
#     colorSet = colors.difference(retiredColors)
#     colorSet = colorSet.union(addedColors)
#     return colorSet
# def createFileOfNewColors(setOfNewColors):
#     orderListOfColors = sorted(getSetOfNewColors)
#
#      = ('\n').join(orderListOfColors)
#     outfile = open("F:\\file\\NewColors.txt",'w')
#     outfile.write(orderListOfColorsString)
#     outfile.close()
# main()

# def main():
#     max = getMax("F:\\file\\numbers.txt")
#     print("the largest number in the \nfile numbers.txt is",str(max) + ".")
# def getMax(filename):
#     infile = open("F:\\file\\numbers.txt",'r')
#     max = int(infile.readline())
#     for line in infile:
#         num = int(line)
#         if num > max:
#             max = num
#     infile.close()
#     return max
# main()

#
# def main():
#     sum = getSum("F:\\file\\numbers.txt")
#     print("the largest number in the \nfile numbers.txt is",str(sum) + ".")
# def getSum(filename):
#     infile = open("F:\\file\\numbers.txt",'r')
#     sum = 0
#     for line in infile:
#         sum += int(line)
#     infile.close()
#     return sum
# main()


#
# def main():
#     numbdigit = getnumbdigit("F:\\file\\numbers.txt")
#     print("the file numbers.txt contains ",str(numbdigit) + " numbers.")
# def getnumbdigit(s):
#     file_name = "F:\\file\\numbers.txt"
#     number_counts = 0
#     with open(file_name, 'r') as f:
#         for line in f:
#                 number_list = [x for x in line.split() if x.isdigit()]
#                 number_counts = len(number_list)
#                 return number_counts
# main()



#
# def main():
#     lastNumber = getLastNumber("F:\\file\\numbers.txt")
#     print("the last number in the \nfile numbers.txt is",str(lastNumber)+".")
# def getLastNumber(fileName):
#     infile = open("F:\\file\\numbers.txt",'r')
#     for line in infile:
#         pass
#     lastNumber = eval(line)
#     infile.close()
#     return lastNumber
# main()


# def main():
#     continent = input("enter the name of a continent: ")
#     continent = continent.title()
#     if continent != "antactica":
#         infile = open("F:\\file\\un.txt",'r')
#         for line in infile:
#             data = line.split(',')
#             if data[1] == continent:
#                 print(data[0])
#     else:
#         print("there are no countries in antactica")
# main()


# def main():
#     d = {}
#     d["spam"] = 3
#     print(d)
#     d.update({"spam":1,"eggs":2})
#     print(d)
#     print("d has",len(d),"items")
#     print("eggs" in d)
#     print("keys:",list(d.keys()))
#     print("values:",list(d.values()))
#     for key in d:
#         print(key,d[key])
#     print(d.get("toast","not in dictionary"))
#     del(d["eggs"])
#     print(d)
# main()


# list1 = [["one",1],["two",2],["three",3]]
# def main():
#     texteseDict = createDictionary("F:\\file\\textese.txt")
#     print("enter a simple sentence in lowercase letters without")
#     sentence = input("any punctuation: ")
#     print()
#     translate(sentence,texteseDict)
# def createDictionary(filename):
#     infile = open(filename,'r')
#     textList = [line.rstrip() for line in infile]
#     infile.close()
#     return dict ([x.split(',') for x in textList])
# def translate(sentence,textesedict):
#     words = sentence.split()
#     for word in words:
#         print(textesedict.get(word,word) + " ",end="")
# main()

# def main():
#     print("enter the person's age group",end="")
#     ageGroup = input("(child , minor ,adult , or senior")
#     print("the admission fee is",determineAmissionFee(ageGroup),"dolaes.")
# def determineAmissionFee(ageGroup):
#     # if ageGroup == "child":
#     #     return 0
#     # elif ageGroup == "minor":
#     #     return 5
#     # elif ageGroup == "adult":
#     #     return 10
#     # elif ageGroup == "senior":
#     #     return 8
#     dict = {"child":0,"minor":5,"adult":10,"senior":8}
#     return dict[ageGroup]
# main()

# def main():
#     listOfWords = formListOfWords("F:\\file\\gettysburg.txt")
#     freq = createFrequencyDictionary(listOfWords)
#     displayWordCount(listOfWords,freq)
#     displayMostCommonWords(freq)
# def formListOfWords(filename):
#     infile = open(filename)
#     originalLine = infile.readline().lower()
#     line = ""
#     for ch in originalLine:
#         if ('a'<=ch<='z') or (ch == " "):
#             line += ch
#         listOfWords = line.split()
#         return listOfWords
# def createFrequencyDictionary(listOfWords):
#     freq = {}
#     for word in listOfWords:
#         freq[word] = 0
#     for word in listOfWords:
#         freq[word] = freq[word]+1
#     return freq
# def displayWordCount(listofwords,freq):
#     print("the gettysburg address contains",len(listofwords),"words.")
#     print("the gettysburg address contains",len(freq),"different words")
#     print()
# def displayMostCommonWords(freq):
#     print("the most cimmon words and thier frequencies are: ")
#     listofmostcommonwords = []
#     for word in freq.keys():
#         if freq[word] >= 6:
#             listofmostcommonwords.sort(key=lambda x:x[1],reverse=True)
#             for item in listofmostcommonwords:
#                 print(" ",item[0] + ': ',item[1])
# main()
#
#




NE={"CT":3.6,"ME":1.3,"MA":6.5,"NH":1.5,"RI":1.1,"VT":0.6}
# print(NE["MA"])
# print(len(NE))
# print(list(NE.keys()))
# print(list(NE.values()))
# print(list(NE.items()))
# print("NH" in NE)
# print(NE.get("PA","absent"))
# print(NE.get("RI","absent"))
# for x in NE:
#     print(x + " ",end = "")
# NE.clear()
# print(NE)
# total = 0
# for x in NE:
#     total += NE[x]
# print("{0:.1f}".format(total))

# newEngland = dict(NE)
# print(newEngland)
# del newEngland["VT"]
# print(newEngland)
# print(len(newEngland))
#

# homeRunKings = {"Bonds":762,"Aaron":755}
# print(len(homeRunKings))
# print(homeRunKings["Aaron"])
# print("Ruth" in homeRunKings)
# print(list(homeRunKings.items()))
# print(min(homeRunKings))
# print(max(homeRunKings))
# print(list(homeRunKings))
# print("Aaron" not in homeRunKings)
# print(list(homeRunKings.values()))
# print(list(homeRunKings.keys()))
# # print(homeRunKings.get("NA"))
# print(homeRunKings.get("NA"))
# for x in sorted(homeRunKings):
#     print(type(x))
# dupHRKs = homeRunKings
# dupHRKs["Bonds"] = 750
# print(homeRunKings["Bonds"])
# newHRKs = {}


# topHitters = {"gehrig":{"atbats":8061,"hits":2721},
#               "ruth":{"atbats":8399,"hits":2873},
#               "williams":{"atbats":7706,"hits":2654}}
# def main():
#     topHitters = {"gehrig": {"atbats": 8061, "hits": 2721},
#                   "ruth": {"atbats": 8399, "hits": 2873},
#                   "williams": {"atbats": 7706, "hits": 2654}}
#     displayBattingAverage(topHitters)
# def displayBattingAverage(topHitters):
#     for hitter in topHitters:
#         print("{0:10} {1:.3f}".format(hitter,topHitters[hitter]["hits"] / topHitters[hitter]["atbats"]))
# main()




# def main():
#     topHitters = {"gehrig": {"atbats": 8061, "hits": 2721},
#                   "ruth": {"atbats": 8399, "hits": 2873},
#                   "williams": {"atbats": 7706, "hits": 2654}}
#     displayBattingAverage(topHitters)
# def displayBattingAverage(topHitters):
#     hitList = []
#     for hitter in topHitters:
#         print(hitter)
#         hitList.append(topHitters[hitter]["hits"])
#         print("hitList:",hitList
#               )
#     value = "{0:.1f}".format(sum(hitList) / len(hitList))
#     print("the average number of hits by")
#     print("the baseball players was",value+'.')
# main()



# 'earl warren':{'pres':'dwight fisenhower','yrleft':1969,'yrappt':1953,'state':'ca'}
#
#
# try:
#     numDependents = int(input("enter number of dependents: "))
# except ValueError:
#     print("\nyou did not respond with an integer value")
#     print("we will assume your answer is zero\n")
#     numDependents = 0
# taxCredit = 1000 * numDependents
# print("tax credit : ",taxCredit)


#
# def main():
#     try:
#         fileName = input("enter the name of a file :")
#         infile = open(fileName,'r')
#         num = float(infile.readline())
#         print(1/num)
#     except FileNotFoundError as exc1:
#         print(exc1)
#     except ValueError as exc2:
#         print(exc2)
# main()
# def main():
#     phoneticAlphabet = {'a':"alpha",'b':"bravo",'c':"charlie"}
#     while True:
#         try:
#             letter = input("enter a,b or c: ")
#             print(phoneticAlphabet[letter])
#             break
#         except KeyError:
#             print("unacceptable letter was entered.")
# main()

#
# def main():
#     total = 0
#     counter = 0
#     foundFlag = True
#     try:
#         infile = open("F:\\file\\numbers.txt",'r')
#     except FileNotFoundError:
#         print("file not found")
#         foundFlag = False
#     if foundFlag:
#         try:
#             for line in infile:
#                 counter += 1
#                 print("counter: ",counter)
#                 total += float(line)
#                 print("total: ",total)
#             print("average: ",total/counter)
#         except ValueError:
#             print("line",counter,"could not be converted to a float.")
#             if counter > 1:
#                 print("average so far : ",total/(counter-1))
#                 print("total so far: ",total)
#             else:
#                 print("no average can be calculated")
#         except ZeroDivisionError:
#             print("file was empty")
#         else:
#             print("total: ",total)
#         finally:
#             infile.close()
# main()


# import os
# def main():
#     createFile()
#     infile = open("F:\\file\\newfile.txt",'r')
#     deleteFile("F:\\file\\newfile.txt")
# def createFile():
#     f = open("F:\\file\\newfile.txt",'w')
#     f.write("hello,world\n")
#     f.close()
# def deleteFile(filename):
#     try:
#         os.remove(filename)
#     except:
#         print("file is open and cannot be deleted.")
# main()



# x = int("1.234")
# f = open("abc.txt",'p')
# x = ['a','b'[2]]
# total = (2+'3')
# x = ['a','b'[2]]
# x = list(range(1,9))[8]
# x = 23
# print(x.startswith(2))
#
# x = 8
# x.append(2)

# {"air","fire","earth","water"}.sort()

# try:
#     num = float(input("enter a number: "))
#     print("your number is : ",num)
# except:
#     print("you must enter a number.")

# nafta = ["canada","united states","mexico"]
# try:
#     print("the third member of NAFTA is ",nafta[3])
# except IndexError:
#     print("error occurred.")
#
# while True:
#     try:
#         n = int(input("enter a nonzero integer: "))
#         reciprocal = 1/n
#         print("the reciprocal of {0} is {1:,.3f}".format(n,reciprocal))
#         break
#     except ValueError:
#         print("you did not enter a nonzero integer.try again")
#     except ZeroDivisionError:
#         print("you entered zero . try again.")

# while True:
#     try:
#         num = int(input("enter an integer from 1 to 100: "))
#         if 1<= num <= 100:
#             print("your number is",str(num) + '.')
#             break
#         else:
#             print("your number was not between 1 and 100.")
#     except ValueError:
#         print("you did not enter an integer")

# import random
# elements = ["earth","air","fire","water"]
# # print(random.choice(elements))
# # print(random.sample(elements,2))
# random.shuffle(elements)
# print(elements)
# # print(random.randint(1,5))



# def main():
#     bankroll = int(input("enter the amount of the bankroll: "))
#     (amount ,timesPlayed) = playDoubleOrNothing(bankroll)
#     print("ending bankroll: ",amount,"dollars")
#     print("number of games played: ",timesPlayed)
# def isOdd(n):
#     if (1<= n<=36) and (n % 2):
#         return True
#     else:
#         return False
# def profit(n):
#     if isOdd(n):
#         return 1
#     else:
#         return -1
# def playDoubleOrNothing(bankroll):
#     amount = bankroll
#     timesPlayed = 0
#     while 0<amount<2*bankroll:
#         n = random.randint(0,37)
#         timesPlayed += 1
#         amount += profit(n)
#     return (amount,timesPlayed)
# main()
#
# def main():
#     for i in range(3):
#         outcome = spinWheel()
#         # print("i:",i)
#         print(outcome,end=" ")
# def spinWheel():
#     n = random.randint(1,20)
#     print("n: ",n)
#     if n>15:
#         return "cherries"
#     elif n>10:
#         return "orange"
#     elif n>5:
#         return "plum"
#     elif n>2:
#         return "melon"
#     elif n>1:
#         return "bell"
#     else:
#         return "bar"
# main()
import random
list1 = [chr(n) for n in range(ord('A') ,ord('Z')+1)]
list2 = random.sample(list1,3)
print(",".join(list2))
