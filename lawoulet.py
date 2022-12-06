from random import randrange

load=input("To quit, press : 0 | Any key to Continue\n")
while load!="0" :
    secret_number = randrange (1, 50) #secret number here
    print("Enter a number between 1 & 50.\n")
    try_times=5
    while try_times>=1 :
        choosen_number = int(input("Guess a number. \n"))
        if choosen_number== secret_number :
            print ("WIN !!!")
            break
        else :
            if choosen_number<secret_number :
                print("The secret number is bigger, guess another one\n")
            else :
                print("The secret number is lower, guess another one\n")
    try_times-= 1
    print ("Number of try left :", try_times)
        
    print("The secret number was :", secret_number)
    load=input("To quit : 0 | Any other key to Continue\n")