main.py
"""

    A chatbot that will serve as a base model for use with any online business.
    This chatbot is my implementation for a brick-and-mortar guitar shop with an online presence

"""

This chatbot is based off the NLTK chat util package with a new implementation to handle method calls and provide more complex answers to the user

In the main class, the pairs are stored to match user input with chatbot replies, including the methods to call.

The reflections that the chatbot uses to replace the user's words from certain responses into replies are also stored here.

The main function simple calls MyChatBot to begin conversing with the user.





In the util package, MyChatBot.py, the implementation of the NLTK chat util is stored.

"""
    This class is my personal implementation of the NLTK chatbot, to include the addition
    of a callback handler to call methods as a reply to user input for more complexity
    and a more intelligent chatbot

"""

Read the documentation at https://www.nltk.org/_modules/nltk/chat/util.html for more info




In the util package there are also 3 classes with methods to be used in replying to the user

agent_connect.py
"""
    This class notifies the user if live support is available or not
    If live support is available, it notifies the user that they have been
    added to the queue

"""

time_in_range checks if the current datetime falls within the allowed days and times, when a live agent would be available

final calls time_in_range and prints out whether an agent is available based on the check



order_results.py

"""
    This class extracts the user input and translates it into a SQL query
    to grab the customer's order info

"""

This class uses mysql.connector to connect to the MySQL database created for the guitar shop, separate from the python files

extractMatchIndex takes the chat match object and finds the indices where the user's response is based on them looking for info on an order #

extractMatchText takes those indices and places the string values from the indicies in the user's response into a new list

findOrder takes the extracted match text and puts it into a SQL query, executes it, fetches the results, and places them into a BeautifulTable table, then into a pandas DataFrame to label the table and print out only specific columns

final takes the user's response object and calls the previous methods to finally print out the end result to the user and display order info



product_list.py
"""
    This class recognizes the request for a product list and creates a SQL query
    to pull product data from the store's database and print it for the customer

"""

This class also uses a mysql.connector to grab info from the guitar shop's database

findProducts does the same thing as findOrder: generates a SQL query, executes, fetches results, places them into a BeautifulTable table, then into a pandas DataFrame and returns the result

final prints the result from findProducts





In the Tests folder, the unit tests to ensure functionality are stored

unitTests.py

"""
    This acts as unit tests for each of the methods uses in the chatbot for more complex
    replies to the user. It is also called if the user asks if the chatbot is broken

"""

test_order establishes controls and test cases, one with the expected result and the other with a method call with a parameter that should produce the expected result. Based on whether the test passes or not, it will return True or False, and print out a pass or fail statement

test_products establishes controls and test cases, one with the expected result and the other with a method call with a parameter that should produce the expected result. Based on whether the test passes or not, it will return True or False, and print out a pass or fail statement

test_agent_connect establishes controls and test cases, one with the expected result and the other with a method call with a parameter that should produce the expected result. Based on whether the test passes or not, it will return True or False, and print out a pass or fail statement

final calls all of the previous tests and if all are True, it prints a pass message. If any fail it will print out a fail message.





Usage


Simply run main.py and begin conversing with the chatbot






Todo:

Implement chatbot into a website


