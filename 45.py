"""
Write a Python program to find the index of an item of a tuple.
"""
def add_to_tuple(input_tuple,item):
    list_convert = list(input_tuple)
    if item in list_convert:
        return list_convert.index(item)
    return 'no item found in tuple'

if __name__ == "__main__":
    findIndexOfItem=input('Enter string to be added')
    print(add_to_tuple(('BBA','BBS','CSIT','BE','BCOM'),findIndexOfItem))