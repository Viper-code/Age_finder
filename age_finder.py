#Please enter only Current or Future when asked to find current age or future age.Please enter
#a year when asked for a year, for this age calculator to work!
import time
opperator = input('Hello and welcome to the Age finder!\nI will find your age in No time and I will tell you your future age!\nEnter If you want to find you current age or you future age just type"Current" for current age and "Future"\nfor future age and I can find ages that people were when they died for example\nJohn was born is 1875 and died in 1979.To find this type of age type "old"\n Type:(current/future/old): ')
if opperator.casefold() == 'current':
    user_year = input("Please enter the year you were born in: ")
    print('Calculating.........')
    time.sleep(1.5)
    calculated = 2020 - int(user_year)
    print("You are " + str(calculated) + ' old')
elif opperator.casefold() == 'future':
    F_year = input('Please enter the future year you want to find you age: ')
    B_year = input('Please enter your birth year: ')
    print('calculating.........')
    time.sleep(1.5)
    F_age = int(F_year) - int(B_year)
    print('You will be ' + str(F_age) + ' years old in ' + F_year + '!' )
elif opperator.casefold() == 'old':
    death_y = input('Please enter the year the person died in: ')
    birth_y = input('Please enter the year the person was born in: ')
    print('calculating..........')
    time.sleep(1.5)
    person_age = int(death_y) - int(birth_y)
    print('He/she was',person_age,'years old when he/she died.')