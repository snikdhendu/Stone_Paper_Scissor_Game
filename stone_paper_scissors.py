import random
list_1=['stone','paper','scissor']


def playgame(round):
    i=0
    user_ch=0
    comp_ch=0
    user_count=0
    comp_count=0
    while(i!=round):
        print("\n")
        print(f"~~~~~~~~~~~~~~~~ ROUND NO:{i+1} ~~~~~~~~~~~~~~~~~~~~")
        print("\n")
        print('''               ---------Enter 1 2 or 3----------
        
                            1.Stone
                            2.Paper
                            3.Scissors''')
        print("\n")
        ch1=int(input( "Choose your turn:"))
        print("\n")
        if(ch1==1):
            user_ch='stone'
        elif(ch1==2):
            user_ch='paper'
        elif(ch1==3):
            user_ch='scissor'
        else:
             print("Invalid choice please enter correct choice")
        comp_ch=random.choice(list_1)
        if(comp_ch==user_ch):
           
            print("You choose:",user_ch,"  ","Computer Choose:",comp_ch)
            print("\n")
            print("############### The Game is Draw ##############")
            print("So,1 point Each")
            user_count=user_count+1
            comp_count=comp_count+1
            print("\n")
            print("Your score :",user_count,"   ","Computer score:",comp_count)
            print("\n")
        
        elif(user_ch=='stone' and comp_ch=='scissor') or (user_ch=='paper' and comp_ch=='stone') or (user_ch=='scissor' and comp_ch=='paper'):
             print("You choose:",user_ch,"  ","Computer Choose:",comp_ch)
             print("\n")
             print("################### so you win :) #################")
             print("You get 1 point")
             user_count=user_count+1
             print("\n")
             print("Your score :",user_count,"   ","Computer score:",comp_count)
             print("\n")
        else:
             print("You choose:",user_ch,"  ","Computer Choose:",comp_ch)
             print("\n")
             print("################## so computer win :( ##################")
             print("computer get 1 point")
             comp_count=comp_count+1
             print("\n")
             print("Your score :",user_count,"   ","Computer score:",comp_count)
             print("\n")
        i=i+1
    if(comp_count>user_count):
        print("Finally Coumter win this Game")
    elif(comp_count<user_count):
        print("Finally You won this Game")
    else:
        print("The final Game is Draw")
    
    print("---------------------------------------------------------------------")
    print("\n")

print('''------------------------ GAME START --------------------------''')
round=0
print("\n")
while(1):
    print('''           1.Enter 1 to play
           2.Enter 2 to exit the game''')
    
    print("\n")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        print("\n")
        round=int(input("Enter how many round you want to play:"))
        playgame(round)
    elif(ch==2):
        exit(0)
    else:
        print("Invalid choice please enter correct choice")

