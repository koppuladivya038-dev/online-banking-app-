# importing all modules
import addition
import subtraction
import multiplication
import division
import modulosDivision

operations = (
    "1. Addition /n",
    "2. Subtraction /n",
    "3. Multiplication /n",
    "4. Division /n",
    "5. Modulus Division"
)


# main function
if __name__ == "__main__":
    print("welcome to simple calculator,it will do two numbers operations")
    choice = int(input("please select your operation(1-6): "))
    while True:
        print(*operations)
    if choice == 1:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        print(addition.add(a = num1, b = num2))
    elif choice == 2:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        print(subtraction.sub(a = num1, b = num2))
    elif choice == 3:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        print(multiplication.mul(a = num1, b = num2))
    elif choice == 4:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        print(division.div(a = num1, b = num2))
    elif choice == 5:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        print(ModulosDivision.modDiv(a = num1, b = num2))
    elif choice == 6:
        print("exiting from calculator")
        exit()
    else:
        print("Please select the operation between 1-6")        
                
                
                
            


            
      
   

