import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

print("Select an operation by using number:")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

operation = input("Select your operation:")


def getNumberValues():
    amountOfNumbers="2"
    if operation=="1" or operation=="3":
        amountOfNumbers = input("How many Numbers:")
    numberamount=int(amountOfNumbers)
    numberList=[]
    for value in range(1,numberamount+1):     
        number=input("Enter the number%d: " %value)
        if number.isnumeric: numberList.append(number) 
        else: logging.warn("this value is not numeric") 
    return numberList


number_list=getNumberValues()

def sumValues():
    result=0
    for number in number_list:
        result=result+float(number)
    return result

def substractValues():
    result=float(number_list[0])-float(number_list[1])
    return result

def multiplyValues():
    result=1
    for number in number_list:
        result=result*float(number)
    return result

def divideValues():
    result=float(number_list[0])/float(number_list[1])
    return result

if operation =="1":        
    logging.debug(f"I'm adding  {number_list}")
    print(f"Sum is {sumValues()}")
elif operation =="2":
    logging.debug(f"I'm substracting {number_list}")
    print(f"The difference is :{substractValues()}")
elif operation=="3":
    logging.debug(f"I'm multiplying {number_list}")
    print(f"Multipication result is :{multiplyValues()}")
elif operation=="4":
    logging.debug(f"I'm dividing {number_list}")
    print(f"Division result is {divideValues()}")