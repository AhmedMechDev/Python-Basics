#function for greet fun(1)
def greet(name , gre="Hallo "):
    print(gre , name)

#function for Calculator fun(2)
def calculator(num1,num2,opp):
    if opp=="+" :
        result=num1 + num2
        return(result)
    elif opp=="-" :
        result=num1 - num2
        return(result)
    elif opp=="/" :
        result=num1 / num2
        return(result)
    elif opp=="*" :
        result=num1 * num2
        return(result)
    else :
        print("ERROR , please try again.")

#function for area of triangle fun(3)
def triangle(b,h):
    area=(1/2)*b*h
    return(area)

#function for area of square fun(4)
def square(side):
    area=side*side
    return(area)

#function for area of rectanguler fun(5)
def rectanguler(length,width):
    area=length*width
    return(area)

#function for area of circle fun(6)
def circle(radius):
    area=3.14*(radius**2)
    return(area)

print("   Welcome to our big Programm :) ")
name1 = input("Chat (Enter your name) : ")
greet(name1)

while True :
    enter= input(" what you need (The calculator or find Area ) ( for stop enter Exit ) : ")
    if enter=="Exit" or enter=="exit" :
        break
    elif enter=="calculator" :
        num1=float(input("Enter the frist number = "))
        num2=float(input("Enter the seconde number = "))
        opp=input("Enter operation (+ , - , / , *) = ")
        re=calculator(num1,num2,opp)
        print(re)
    elif enter=="area" or enter=="Area" :
        ent=input("Enter which area you need (triangle , square , rectanguler , circle) = ")
        if ent=="triangle" :
            b=float(input("Enter the base = "))
            h=float(input("Enter the height = "))
            ar=triangle(b,h)
            print(ar)
        elif ent=="square" :
            side=float(input("Enter the number of side = "))
            ar=square(side)
            print(ar)
        elif ent=="rectanguler" :
            lenght=float(input("Enter the lenght = "))
            width=float(input("Enter the width = "))
            ar=rectanguler(lenght,width)
            print(ar)
        elif ent=="circle" :
            raduis=float(input("Enter the reduis = "))
            ar=circle(raduis)
            print(ar)
        else : 
            print("ERROR , please try again.")