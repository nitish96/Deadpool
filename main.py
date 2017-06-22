from spy_details import spy
from add_status import add_status1
from add_buddy import add_buddy1
from message import send_message, read_message, read_chat_history

print 'Let\'s get started'

user_exists = raw_input('Do you want to continue as' + spy ['salutation'] + ' ' + spy['name'] + '(Y/N)')


def start_app(spy):

    current_status_message = None

    if spy['age'] > 12 and spy['age'] < 50:

        if spy['rating'] >= 0.0 and spy['rating'] < 2.5:
            print'Authentication completed. Welcome %s %s, age : %d.' \
                  ' Proud to have you on board. You are a noobie' \
                   % (spy['salutation'], spy['name'], spy['age'])
        elif spy['rating'] >= 2.5 and spy['rating'] < 4.0 :
            print'Authentication completed. Welcome %s %s, age : %d. ' \
                 'Proud to have you on board. You are an intermediate' \
             % (spy['salutation'], spy['name'], spy['age'])
        elif spy['rating'] >= 4.0:
            print'Authentication completed. Welcome %s %s, age : %d. ' \
                 'Proud to have you on board. You are an expert' \
             % (spy['salutation'], spy['name'], spy['age'])

        show_menu = True

        while show_menu:

            menu_choices = "What do you want to do?\n" \
                           "1. Add a status update\n" \
                           "2. Add a friend \n" \
                           "3. Send a secret message \n" \
                           "4. Read a secret message\n" \
                           "5. Read Chats from a user \n" \
                           "6. Close Application \n"

            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    current_status_message = add_status1(current_status_message)

                elif menu_choice == 2:
                    number_of_friends = add_buddy1()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
                    print'Enter a valid option'
    else:
       print'Sorry you are not of the correct age to be a spy'


if user_exists.upper() == "Y":
    start_app(spy)
elif user_exists.upper() == "N":
    spy= {
        'name' : '',
        'salutation': '',
        'age' : 0,
        'rating' : 0.0,
        'is_online' : False
    }

    spy['name'] = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy['name']) > 0:
        spy['salutation'] = raw_input("Should I call you Mr. or Ms.?: ")

        spy['age'] = raw_input("What is your age?")
        spy['age'] = int(spy['age'])

        spy['rating'] = raw_input("What is your spy rating?")
        spy['rating'] = float(spy['rating'])

        spy['is_online'] = True
        start_app(spy)
    else:
        print 'Please add a valid spy name'
else:
    print 'Not a valid input'