''' a program for using the try keyword in python '''
c=0 #counting variable
w=0 # warning variable
while(True): # loop for contiuing the game
    a=input("enter the number : ")

    if a == 'q': # exiting the loop
        break
    try:

        a=int(a)
        if a<23:
            print("increased the bot points >>>")
            c=c+1
        else:
            print(" decreased the bot points .>>>>")
            c=c-1
    except Exception as e: # handling the exception
        w=w+1

        print(e)

        print(" please enter only numerical input or else you ll be loosing the game ")
        if w>3:
            c=-1
            print("Lost , out of warning ")
            break

print("final score board:",c)
if c<0:
    print("lost dammmnn!!!")
else:
    print("won wohooooo!!!")
print("thanks for playing the game>>>>>>")

