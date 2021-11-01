# Exercise 1 : Call History
# Instructions

# Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)

# Test your code !!!
# -------------------------------
class Phone:
    # Create a class called Phone. This class takes a parameter called phone_number. 
    # When instantiating an object create an attribute called call_history which value is an empty list.
    # Add another attribute called messages to your __init__() method which value is an empty list.
    def __init__(self, phone_number):
        self.number = phone_number
        self.call_history = []
        self.messages = []

    # Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. 
    # The method should print a string stating who called who, and add this string to the phone’s call_history.
    def phone_call(self, other_phone):
        call_string= f"Call from {self.number}, to: {other_phone.number}"
        # print(call_string)
        self.call_history.append(call_string)
        other_phone.call_history.append(call_string)

    # Add a method called show_call_history. This method should print the call_history.
    def show_call_history(self):
        for record in self.call_history:
            print(f"Phone history of {self.number} is: \n{record}")

    # Create a method called send_message which is similar to the call method. 
    # Each message should be saved as a dictionary with the following keys:
    # to
    # from
    # content
    def send_message(self, other_phone, content):
        if content:
            message = {
            'to': other_phone.number,
            'from': self.number,
            'content': content,
            }
            self.messages.append(message)
            other_phone.messages.append(message)
        else:
            print("You cannot send an empy messege...")
    # messege history for self number
    def show_outgoing_messege(self):
        print("-------OUTGOING MESSAGES-----")
        for message in self.messages:
            if message['from'] == self.number:
                print(f"Sending to: {message['to']}\nContent:{message['content']}")
                print("------END---------")
    # messege history for other number
    def show_incoming_messege(self):
        print("-----INCOMING MESSAGES----")
        for message in self.messages:
            if message['from'] == self.number:
                print(f"From: {message['from']}\nContent: {message['content']}")
                print("--------END-------------")

phone1 = Phone('123456789')
phone2 = Phone('987654321')

phone1.phone_call(phone2)
phone2.phone_call(phone1)

# phone1.show_call_history()
# phone2.show_call_history()

phone1.send_message(phone2, "hello phone 2")
phone2.send_message(phone1, 'hello phone 1')

phone1.show_outgoing_messege()
phone2.show_outgoing_messege()


phone1.show_incoming_messege()
phone2.show_incoming_messege()


