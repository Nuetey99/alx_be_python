def perform_operation(num1, num2, operation):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "division":
        if num1 or num2 == 0:
            print ("Division error!")
        else :
                result = num1/num2
    elif operation == "multiplication":
         result = num1*num2
         
       
         
                   