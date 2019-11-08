#!/usr/bin/python3

def multiplication(arg_a, arg_b):
    return arg_a * arg_b

def division(arg_a, arg_b):
    try:
        result = arg_a/arg_b
        return result
    except ZeroDivisionError:
        print('erreur de devision par zero')


