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
# b




p158 t85
对列表的数字进行  位数之和进行升序排列  展示出来
array = [865, 1169, 1208, 1243, 329]
# 定义取和
def a_sun(number):
    t1 = number % 10
    l1 = number // 10
    t2 = l1 % 10
    l2 = l1 // 10
    t3 = l2 % 10
    l3 = l2 // 10
    t4 = l3 % 10
    asum = t1 + t2 + t3 + t4
    return asum
def a_des(array):
    for d in range(0, len(array)):
        for i in range(0, len(array)):
            if a_sun(array[i]) > a_sun(array[d]):
                array[d], array[i] = array[i], array[d]
a_des(array)
print(array)
