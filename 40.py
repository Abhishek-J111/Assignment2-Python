"""
Write a Python program to add an item in a tuple.
"""
def add_to_tuple(input_tuple,item):
    list_convert = list(input_tuple)
    list_convert.append(item)
    return(tuple(list_convert))

if __name__ == "__main__":
    itemtoEnter=input('Enter string to be added')
    print(add_to_tuple(('BBA','BBS','CSIT','BE','BCOM'),itemtoEnter))