#!/usr/bin/env python3

def happy_new_year():
    count = 10

    while count > 0:
        print(count)
        count-=1
    print("Happy New Year!")


def square_integers(int_list):
    sqInts = list()
    for i in int_list:
        sqInts.append(i*i)
    
    return sqInts

def fizzbuzz():
    count = 1
    while count <= 100:
        txt = ""
        if (count%3 == 0):
            txt += "Fizz"
        if (count%5 == 0):
            txt += "Buzz"
        
        if(txt == ""):
            print(count)
        else:
            print(txt)

        count+=1

        

        
