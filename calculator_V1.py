import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile1.log")

print("Select an operation by using number:")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

operation = input()
num1=input("Enter the first number:")
num2=input("Enter the second number:")


if operation =="1":        
    logging.debug(f"I'm adding {num1} + {num2}")
    print("The sum is :"+ str(float(num1)+float(num2)))
elif operation =="2":
    logging.debug(f"I'm substracting {num1} - {num2}")
    print("The difference is :"+ str(float(num1)-float(num2)))
elif operation=="3":
    logging.debug(f"I'm multiplying {num1} * {num2}")
    print("The result is :"+ str(float(num1)*float(num2)))
elif operation=="4":
    logging.debug(f"I'm dividing {num1} / {num2}")
    print("The division result is :"+ str(float(num1)/float(num2)))
  