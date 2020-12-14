import email_example


def incomingcall():
    incoming_call = int(input("Type the tag displayed on the caller ID "))
    if incoming_call == 1:
        email_example.example()
    else:
        print("Value selected does not exist")


incomingcall()
