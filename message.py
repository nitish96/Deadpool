
from steganography.steganography import Steganography
from datetime import datetime
from spy_details import buddy
def choose_a_friend():

    item_choice = 0

    for bud in buddy:
        print '%d. %s' % (item_choice + 1, bud['name'])
        item_choice = item_choice + 1

    bud_selection = raw_input('Choose from your fellow spies')
    if len(bud_selection) > 0:
        bud_selection = int(bud_selection)
        return bud_selection

def send_message():

    bud_choice = choose_a_friend()
    bud_choice_position = int(bud_choice) - 1

    original_image = raw_input("What is the name of the image?")
    output_path = "eifel.jpg"
    text = raw_input("What do you want to say? ")
    if len(text) > 50:

        del buddy[bud_choice_position]
    elif len(text) == 0:
        print 'please enter some text'
    else:
        Steganography.encode(original_image, output_path, text)

        new_chat = {
            "message": text,
            "time": datetime.now(),
            "sent_by_me": True
            }
        buddy[bud_choice]['chats'].append(new_chat)

        print "Your secret message image is ready!"

def read_message():

    sender = choose_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    buddy[sender]['chats'].append(new_chat)

    print "Your secret message has been saved!"

def read_chat_history():

    buddy_name = choose_a_friend()
    for chat in buddy[buddy_name]['chats']:
        if chat['sent_by_me']:
            print '[%s]: %s %s.'%(chat['time'].strftime("%d.%B,%Y") ,"You said" ,chat['message'])
        else:
            print '[%s] %s said: %s' % (chat['time'].strftime("%d %B %Y"), buddy[buddy_name]['name'], chat['message'])
