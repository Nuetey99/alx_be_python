import random

player_name = input("Enter player name: ")
player_age = int(input("Enter player age:"))
player_choice = input("Do you want to play? (YES/NO)").lower()

while player_choice == "yes" : 
if player_age >= 18 :
        print("Greetings!", player_name)

       
            secret_number = random.randint(1,8)
            guess_number = int(input("Pick your number: "))
   
        if guess_number == secret_number:
                print("Congratulations, you guessed it!")
        elif secret_number < guess_number-3 or secret_number < guess_number-4 or secret_number < guess_number-5:  
                print("Oops, your guess is a bit high. Try again!")
        elif secret_number > guess_number-3 or secret_number < guess_number-4 or secret_number < guess_number-5
                print("Oops, your guess is a bit low. Try again!")

else :
        print("GET OUTTA HERE!!!",player_name)


