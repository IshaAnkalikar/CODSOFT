import random
print('ROCK PAPER SCISSORS GAME')
print('Choose any one option:1.ROCK\n2.PAPER\n3.SCISSORS')
print('''Rules of the game are:
     Rock beats scissorS
     scissors beat paper
     paper beats rock''')
choice=int(input('Enter your choice'))
if choice==1:
     choice_name='rock'
elif choice==2:
     choice_name='paper'
elif choice==3:
     choice_name='scissors'
else:
     print('Invalid choice')
print('Users choice is',choice_name)
print('Now its computers turn')
computer_choice=random.randint(1,3)
if choice==computer_choice:
     computer_choice=random.randint(1,3)
     if computer_choice==1:
          computer_choice_name='Rock'
     elif computer_choice==2:
          computer_choice_name='Paper'
     elif computer_choice==3:
          computer_choice_name='Scissors'
     else:
          print('Its a tie!!!')
if choice==1 and computer_choice==2:
     print('Paper wins!!',end='')
elif choice==2 and computer_choice==3:
     print('Scissors win!!',end='')
else:
     print('Rock wins!!',end='')

print('Thank you for playing.')







            
                


  
           
