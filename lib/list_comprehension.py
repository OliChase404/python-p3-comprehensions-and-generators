#!/usr/bin/env python3

# def return_evens(num_list):
#     evens = []
#     for i in num_list:
#         if(i % 2 == 0):
#             evens.append(i)
#     return evens

# def make_exclamation(sentence_list):
#     exclamations = []
#     for i in sentence_list:
#         exclmations.append(i + '!')
#     return exclmations
        
        
        
def make_exclamation(sentence_list):
    excl = [(i + '!') for i in sentence_list]
    return excl


def return_evens(num_list):
    return [i for i in num_list if i % 2 == 0]
