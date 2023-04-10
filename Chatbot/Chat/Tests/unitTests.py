"""
    This acts as unit tests for each of the methods uses in the chatbot for more complex
    replies to the user. It is also called if the user asks if the chatbot is broken

"""

import datetime
import util
import sys

sys.path.append('..')


def test_order():
    control = '   Order #          Order Date Ship $  Tax $           Ship Date Card Expiration Date' \
              '\n0        1 2018-03-28 09:40:28   5.00  32.32 2018-03-30 15:32:51              04/2020'
    case = str(util.order_results.findOrder(1))
    if case == control:
        print("Order Test Passed")
        return True
    else:
        print("Order Test Failed")
        return False


def test_products():
    control = "                           Product Name Product Price $\n" \
              "0                   Fender Stratocaster          699.00\n" \
              "1                       Gibson Les Paul         1199.00\n" \
              "2                             Gibson SG         2517.00\n" \
              "3                         Yamaha FG700S          489.99\n" \
              "4                         Washburn D10S          299.00\n" \
              "5                Rodriguez Caballero 11          415.00\n" \
              "6                      Fender Precision          799.99\n" \
              "7                           Hofner Icon          499.99\n" \
              "8  Ludwig 5-piece Drum Set with Cymbals          699.99\n" \
              "9    Tama 5-Piece Drum Set with Cymbals          799.99"
    case = str(util.product_list.findProducts(None))
    if case == control:
        print("Product Test Passed")
        return True
    else:
        print("Product Test Failed")
        return False


def test_agent_connect():
    start = datetime.time(8, 0, 0)
    end = datetime.time(20, 0, 0)
    test_fail_time = datetime.datetime(2023, 5, 5, 5, 0, 0)
    test_pass_time = datetime.datetime(2023, 4, 5, 14, 0, 0)
    if not util.agent_connect.time_in_range(start, end, test_fail_time) \
            and util.agent_connect.time_in_range(start, end, test_pass_time):
        print("Agent Connect Test Passed")
        return True
    else:
        print("Agent Connect Test Failed")
        return False


def final(match):
    if test_order() and test_products() and test_agent_connect():
        print('All tests passed. Chat functioning correctly')
    else:
        print('One or more tests failed. Please contact an administrator')
