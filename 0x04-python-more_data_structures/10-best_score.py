#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = float('-inf')
    best_key = None
    if a_dictionary != None:
        for key, value in a_dictionary.items():
            if value > best_score:
                best_score = value
                best_key = key
    return best_key
        
