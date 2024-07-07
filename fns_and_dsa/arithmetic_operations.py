def perform_operation(num1, num2, operation):
     match operation:
          case "add":
               return num1+num2
          case "subtract":
              return num1-num2
          case "multiplication":
               return num1*num2
          case "division" :
               if num1 or num2 == 0:
                    print ("Division error!")
               else :
                   return num1/num2
          case _:
               print("An error occurred!")


         
                   