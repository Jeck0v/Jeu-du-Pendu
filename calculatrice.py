def add(num1, num2):
  return num1 + num2
def sub(num1, num2):
  return num1 - num2
def multi(num1, num2):
  return num1 * num2
def div(num1, num2):
  return num1 / num2
while True:
  operation = input("Enter operation (+, -, *, /): ")
  if operation not in ['+', '-', '*', '/']:
      print("Invalid operation. Try again.")
      continue

  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))

  if operation == '+':
      result = add(num1, num2)
  elif operation == '-':
      result = sub(num1, num2)
  elif operation == '*':
      result = multi(num1, num2)
  elif operation == '/':
      result = div(num1, num2)

  print("Result: ", result)
