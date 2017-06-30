from datetime import datetime

#spy name list
class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

#here is the block of who send the message
class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

#Here is the list of friends
spy = Spy('Amar', 'Mr.', 20, 4.1)
friend_one = Spy('Manish', 'Mr.', 22, 4.9)
friend_two = Spy('Joney', 'Mr.', 23, 3.7)
friend_three = Spy('Rajnish', 'Mr.', 21, 3.1)

friends = [friend_one, friend_two, friend_three]
