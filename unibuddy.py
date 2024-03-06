
# initialize the first message
print('Welcome to UniBuddy chatbot.\nPlease enter your credentials to start :')

while True:
    user_name = input('Please enter your name:\t').capitalize()

    # Check if user_name is empty or consists only of whitespace
    if not user_name.strip():
        print('Invalid username. Please enter your name again.')
        continue

    # Check if user_name consists only of digits
    if user_name.isdigit():
        print('Invalid username. Please enter a name, not a number.')
        continue

    # If the input is valid, break the loop
    break


while True:
    try:
        age = int(input('Please enter your age:\t'))
        break # Break the loop if input is successfully converted to an integer
    except ValueError:
        print('Invalid input. Please enter a number.')

    
# Greeting and activities based on favorite color
print(f'Hello {user_name}, Welcome to our support system.\n')

while True: 

    fav_colour = input('We have Blue, Yellow and Red activity campuses in here.\nplease enter your favourite colour:\t').capitalize()

    if fav_colour == "Blue":
        print('\nOur Blue compus includes the below activities:')
        print(''' 
1. Uni Swimming Regional team. 
2. Uni Club Water Polo.
3. Uni Rowing Cotter Club. 
4. Uni Diving High team. 
''')
        break

    elif fav_colour == "Red":
        print('\nOur Red compus includes the below activities:')
        print(''' 
1. Junior ManU Footbal club. 
2. Hampshire Kricket Club.
3. Ground Wrestling Club. 
4. Uni special Daart team. 
''')
        break

    elif fav_colour == 'Yellow':
        print('\nOur Yellow compus includes the below activities:')
        print(''' 
1. Genius Chest club. 
2. Robotic Uni Club.
3. Fantastic Book Club. 
4. Uni Match making team. 
''')
        break


    else:
        print('Please enter only "Blue", "Yellow", or "Red".')


# Recommendations based on age
if 18 <= age <= 19: 
    print('Also, it seems you are new here and may need more help with events:')
    print('''
1. Showing the whole University with Katherina.
2. Session to know more about the library. 
3. Introducing to the support team.
4. Campus tour with the Student Union representatives.
5. Joining a study group for your first semester courses.
''')


elif 19 < age > 22: 
    print('If you would like to know more about new programs for this semester:')
    print('''
1. Please log in to your student portal and check out the new events.
2. Joining a sports team or club.
3. Participating in career development workshops.
4. Attending social events organized by the university.
5. Exploring internship opportunities in your field of study.
''')


else:
    print('Please feel free to reach out to the support team for more information.')

# F&Q : Asking users 
    
question = input('Is there anything else you would like to ask me? Press Q to exit: ').capitalize()

if question == 'How do I reset my password?':
    print('\nYou can reset your password by visiting our website and clicking on the "Forgot Password" link.')

elif question == 'How can I contact the support team?':
    print('\nYou can contact the support team by emailing support@unibuddy.com or calling our helpline at 1-800-UNIBUDDY.')
    
elif question == 'What are the office hours of the support team?':
    print('\nOur support team is available from Monday to Friday, 9:00 AM to 5:00 PM.')

elif question == 'Q':
    print('\nI am glad I could be helpful. Please feel free to use this chatbot if you have any questions.')

else:
    print('\nPlease reach out to the support team at the front desk to help with your queries.')



