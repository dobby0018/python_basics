# user_input = input("Enter a number: ")
# try:
#     user_number = float(user_input)
#     print(f"You entered the number {user_number}")
# except ValueError:
#     print("That's not a valid number.")
    
    # second
try:
    x = int(input("Enter a number: "))
    result = 10 / x
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
except:
    print("enter the correct value")
else:
    print(f"Result: {result}")
finally:
    print("Execution complete.")
