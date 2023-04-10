"""

    A chatbot that will serve as a base model for use with any online business.
    This chatbot is my implementation for a brick-and-mortar guitar shop with an online presence

"""
from Tests import unitTests
from util import order_results, product_list, agent_connect
from util.MyChatBot import MyChatBot
import sys

sys.path.append('..')

pairs = [
    ['(.*)my name is (.*)', ['Hello, %2', 'Hi, %2', 'Nice to meet you, %2'], None],
    ['(.*)my names (.*)', ['Hello, %2', 'Hi, %2', 'Nice to meet you, %2'], None],
    ['(.*)my name\'s (.*)', ['Hello, %2', 'Hi, %2', 'Nice to meet you, %2'], None],
    ['(i\'m bored|im bored|(.*)boring)', ['Hello, %1, I\'m dad'], None],
    ['(.*)thank(.*)', ['My pleasure!'], None],
    ['(you suck|this sucks|stupid|lame|dumb|annoying)', ['Sorry you feel that way. Please use code \'ANNOYED\' '
                                                         'for $1 off your next purchase'], None],
    ['(wow|rude|not cool|how dare you|whoa)', ['Sorry!'], None],
    ['(robot egg|chatbot egg|(.*)surprise me|(.*)tell me a secret)', ['You found the easter egg! Enjoy $10 off your '
                                                                      'next purchase with code \'EGG\'!'], None],
    ['(hi|hello|hey)', ['Hey there', 'Hello!', 'Hi', 'How are you?', 'Hi! What is your name?'], None],
    ['(how are you|how is it going|how\'s it going|hows it going)', ['I\'m doing well! Can I help you with anything?'
                                                                     'Hint: type \'help\''], None],
    ['(where is|my order|order|order help|help with order|find my order)', ['Enter your order number for info. '
                                                                            'Example: \'#2\''], None],
    ['# (.*)', ['Anything else I can help you with?'], order_results.final],
    ['#(.*)', ['Anything else I can help you with?'], order_results.final],
    ['(.*)products(.*)', ['Anything else I can help you with?'], product_list.final],
    ['(.*)hours(.*)', ['The brick and mortar store is open:\nMonday through Fridays 8am to 8pm\nSaturday and '
                       'Sundays 10am to 6pm.\nThe online store is open 24 hours a day; however, live support agents'
                       ' are only available Monday through Friday 8am to 8pm.'
                       '\n\nI am happy to help you anytime!'], None],
    ['((.*)live agent(.*)|(.*)agent(.*)|customer support)', ['Anything else I can help you with?'],
     agent_connect.final],
    ['(help|(.*)what can you do(.*)|options|what do you do|useless|uses)', ['Some available prompts you can try are '
                                                                            'asking for \'Store hours\', \'Products\', '
                                                                            '\'Find my order\', \'Connect with live '
                                                                            'agent\', \'Test connection\''],
     None],
    ['(test connection|is this working|(.*)broken|not working|test)', ['It seems I am working just fine. '
                                                                       'Anything else I can help you with? Hint: '
                                                                       'Type \'help\''], unitTests.final],
    ['((.*)joke|tell me a joke|(.*)funny|humor)', ['How can a leopard change his spots?\n'
                                                   '...By moving!',
                                                   'Why did the user ask for a joke?\n'
                                                   '...Because he wants to laugh at '
                                                   'something that’s not his bank balance.',
                                                   'Why did the chatbot not know the answer?\n'
                                                   '...It was a chatbot, not a search engine.',
                                                   'Why did the robot chicken cross the road?\n'
                                                   '...It was trying to find out how much it was going '
                                                   'to cost to make that joke.',
                                                   'Why was the chatbot created?\n'
                                                   'Apparently, some people want to talk to a robot, but they don’t '
                                                   'want to '
                                                   'talk to a person.',
                                                   'What did the chatbot say to the other chatbot?\n'
                                                   'Finally, something that makes sense!'], None],
]

my_reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
    "they": "them",
    "bot": " ...Wait, you're a bot too?!",
    "chatbot": " ...Wait, you're a bot too?!"
}


def main():
    chat = MyChatBot(pairs, my_reflections)
    chat.converse()


if __name__ == "__main__":
    main()
