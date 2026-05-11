print("1 - add")
print("2 - substraction")
print("3 - multipliction")
print("4 - division")
option = int(input("choose an operation :"))
result = 0
if (option in [1,2,3,4]):
  num1 = int(input("enter the first number"))
  num2 = int(input("enter the second number"))
  if (option =1):
    result = num1 + num2
    elif(option = 2):
      result = num1 - num2
      elif(optin = 3):
        result = num1 * num2
        elif(optin = 4):
          result = num1 // num2
          
else:
  print("invalid operation")
print(" the result of the operation is {}".format(result))
  
