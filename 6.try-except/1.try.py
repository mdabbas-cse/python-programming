userInput = input("Enter user input: ")
try:
    if userInput.isdigit():
        print("number is allowed")
except Exception as e:
  print("Ow no, something went wrong", e)
