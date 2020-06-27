"""
Write a Python program to multiply all the items in a dictionary.
"""
from functools import reduce
def mul_dict(input_dict):
    return reduce(lambda a,b:a*b ,input_dict.values())
        
if __name__ == "__main__":
    print(mul_dict({1:10, 2:20, 3:30, 4:40, 5:50}))