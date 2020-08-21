print('!!!!!--BIG BOYS BIKE SHOP  [BBB]--!!!!!')
bike=5
opt=('y')
while bike<=10:
    print('for Hayabusa press - 1 \n'.upper())
    print('for ktm press -2 \n'.upper())
    print('for Ducati press -3 \n'.upper())
    print('for Scooty press -4 \n'.upper())
    option=int(input('choose any one :  '))

    if option==1:
        print('sir the prize for hayabusa is upto - 10lakhs  \n')
        print('sir, can we proccesed further  \n')
        opt=(input('yes,no:  '))
        if opt ==("y"):
            print(input('how would you pay =  \n'))
            print('thank you so much ')
            break
        elif opt ==("n"):
            print('ty')
        else:
            print('--sorry try again--')
            break
    if option==2:
        print('sir the prize for KTM is upto - 1.5lakhs  \n')
        print('sir, can we proccesed further  \n')
        opt = (input('yes,no:  '))
        if opt == ("y"):
            print(input('how would you pay =  '))
            print('thank you so much ')
            break
        elif opt == ("n"):
            print('ty')
        else:
            print('--sorry try again---')
            break

    if option==3:
        print('sir the prize for Ducati is upto - 15lakhs  \n')
        print('sir, can we proccesed further  \n')
        opt = (input('yes,no:  '))
        if opt == ("y"):
            print(input('how would you pay =  '))
            print('thank you so much ')
            break
        elif opt == ("n"):
            print('ty')
        else:
            print('--sorry try again---')
            break

    if option==4:
        print('sir the prize for scooty is upto - 50k  \n')
        print('sir, can we proccesed further  \n')
        opt = (input('yes,no:  '))
        if opt == ("y"):
            print(input('how would you pay =  '))
            print('thank you so much ')
            break
        elif opt == ("n"):
            print('ty')
        else:
            print('--sorry try again---')
            break

print(input('Full Name=  '))
print(input('Contact Number=  '))

print("""Thank you for visiting our shop ,
your bike will be soon dispatched --
            """)




