def add(num1,num2):
    return(num1+num2)
def sub(num1,num2):
    return(num1-num2)
def mul(num1,num2):
    return(num1*num2)
def divide(num1,num2):
    if num2==0:
        return("invaild")
    return(num1/num2)


num1=float(input("Enter_first_digit:"))
num2=float(input("Enter_second_digit:"))

print("select_opretion")
print("1.addition")
print("2.subtraction")
print("3.multiply")
print("4.divide")


choose=int(input("operation:"))


if choose==1:
    print("result:",add(num1,num2))

elif choose==2:
    print("result:",sub(num1,num2))

elif choose==3:
    print("result:",mul(num1,num2))

elif choose==4:
    print("result:",divide(num1,num2))

else:
    print("invailed_input")
