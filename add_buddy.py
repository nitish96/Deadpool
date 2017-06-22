from spy_details import spy, buddy

def add_buddy1():

    new_buddy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'chats': []
    }

    new_buddy['name'] = raw_input('please add your friends name')
    new_buddy['salutation'] = raw_input('Choose Mr or Ms')
    new_buddy['age'] = int(raw_input('Enter the age of your friend'))
    new_buddy['rating'] = float(raw_input('Enter the rating of your friend'))

    if len(new_buddy['name']) > 0 and new_buddy['age'] > 12 and new_buddy['rating'] >= spy['rating']:
        buddy.append(new_buddy)
        print 'Friend Added'

    else:
        print 'Your friend is not good enough.'
    return len(buddy)
