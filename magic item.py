#a program for genrating random magic item prices#
#imports and other start crud#
import random

#frount screen#
print("hello, welcome to magic items pricing")
common = input("number of common items:")
uncommon = input("number of uncommon items:")
rare = input("number of rare items:")
very_rare = input("number of very rare items:")
legendary = input("number of legendy items:")

#convert to interger#
common = int(common)
uncommon = int(uncommon)
rare = int(rare)
very_rare = int(very_rare)
legendary = int(legendary)

#genrate prices#
#def genrate_prices()#

    #common#
print("common prices")
for n in range(common):
    print(random.randrange(50, 100))

#uncommon
print("uncommon prices")
for n in range(uncommon):
    print(random.randrange(101, 500))

#rare#
print("rare prices")
for n in range(rare):
    print(random.randrange(501, 5000))
    
#very rare#
print("very rare prices")
for n in range(very_rare):
    print(random.randrange(5001, 50000))
    
#legendy#
print("legendery prices")
for n in range(legendary):
    print(random.randrange(50001, 1000000))