#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    product_list = []  # List to store products of each tuple
    second_values = []  # List to store second elements of each tuple
    for tuple_item in my_list:
        first_element, second_element = tuple_item
        product_list.append(first_element * second_element)
        second_values.append(second_element)
    return sum(product_list) / sum(second_values)
