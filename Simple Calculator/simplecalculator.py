def add(num1,num2):
    """Add two numbers."""
    return num1+num2

def sub(num1,num2):
    """Subtract num2 from num1."""
    return num1-num2

def mul(num1,num2):
    """Multipy two numbers."""
    return num1*num2

def div(num1,num2):
    """Divide num1 by num2,handling division by zero."""
    if num2!=0:
     return num1/num2
    else:
        raise ZeroDivisionError("Cannot divide by zero")

def get_valid_input(prompt):
    while True:
        try:
            value=float(input(prompt))
            return value
        except ValueError:
            print("Invalid input.Please enter a valid number.")

def SimpleCal():
    print("-----------------Simple Calculator------------------------")
    
    operations={
        '1': {'operator': '+', 'function': add},
        '2': {'operator': '-', 'function': sub},
        '3': {'operator': '*', 'function': mul},
        '4': {'operator': '/', 'function': div}, 
    }
    while True:
        print("Select operation:")
        for key, value in operations.items():
            print(f"{key}. {value['operator']}")
        print("5. Exit")
        
        choice=input("Enter Your Choice(1/2/3/4/5):")
        if choice=='5':
            print("You have decided to exit.Goodbye!")
            break
        if choice in operations:
            num1=get_valid_input("Enter the first number:")
            num2=get_valid_input("Enter the second number:")

            try:
                    result=operations[choice]['function'](num1,num2)
                    operator=operations[choice]['operator']
                    print(f"{num1}{operator}{num2}={result}")
            except ZeroDivisionError as e:
                    print(e)

        else:
             print("Invalid input.Please enter a valid choice.")
if __name__=="__main__":
    SimpleCal()