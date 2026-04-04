try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    result = num1/num2

except ZeroDivisionError:
    print("Can't divide with zero") 

except ValueError:
    print("Enter valid num")

else:
    print("Division : ",result) 

finally:
    print("This block always run")              
