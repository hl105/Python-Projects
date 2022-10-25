print("Let's practice some math!")

# Get inputs and convert them to integers:
firstNum = input('Enter an integer between 1 and 20: ')
firstNum = int(firstNum)
secondNum = input('Enter another integer between 1 and 20: ')
secondNum = int(secondNum)

# Print a blank line:
print()

# Print some info about the numbers:
print('The numbers you entered are', firstNum, 'and', secondNum)
print('The larger number is', max(firstNum, secondNum))
print('The smaller number is', min(firstNum, secondNum))
print('These bars show how big they are:')
print('=' * firstNum)
print('=' * secondNum)
print() # Blank line 

# Test sum:
prompt = '[Addition] What is ' + str(firstNum) + '+' + str(secondNum) + ' ? '
input(prompt) # Note: we intentionally don't store or check the result
sumResult = firstNum + secondNum
print('[Addition] The answer is:', sumResult)
print() # Blank line
 

# Test difference:

prompt = '[Subtraction] What is ' + str(firstNum)+ '-' + str(secondNum) + ' ? '
input(prompt)
diffResult = firstNum - secondNum
print('[Subtraction] The answer is:', diffResult)
print() # Blank line

# Test product:
prompt = (
    '[Multiplication] What is '
  + str(firstNum) + '*'
  + str(secondNum) + ' ? '
)
input(prompt)
prodResult = firstNum * secondNum
print('[Multiplication] The answer is: ' + str(prodResult))
print()


# Test division and remainder:
divString = str(firstNum) + '/' + str(secondNum)
prompt1 = '[Division] What is ' + divString + ' (rounded to an integer)? '
prompt2 = '[Remainder] What is the remainder of ' + divString + ' ? '
input(prompt1)
divResult = round(firstNum / secondNum)
print('[Division] The answer is:', divResult)
print() # Blank line

input(prompt2)
remResult = firstNum % secondNum
print('[Remainder] The answer is:', remResult)
