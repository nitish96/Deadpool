STATUS_LIST = ['hey there i am using python', 'Hello, I am a programmer']

def add_status1(current_status_message):

    updated_status_message = None

    if current_status_message is not None:
        print 'your current message is %s' % current_status_message
    else:
        print "You do not have any status messages"

    query = raw_input("Do you want to choose from the per existing statuses? (Y/N)")

    if query.upper() == "Y":

        for message in range(0, len(STATUS_LIST)):

            print '%s' % (STATUS_LIST[message])

        status_selection = raw_input('Enter the serial number of status that you want to select')
        if len(status_selection) > 0:
            status_selection = int(status_selection)
            updated_status_message = STATUS_LIST[status_selection-1]

    elif query.upper() == "N":
        new_status = raw_input("please enter your new status")

        if len(new_status) > 0:
            STATUS_LIST.append(new_status)
            updated_status_message = new_status

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % updated_status_message
    else:
        print 'You did not update your status message'

    return updated_status_message
