"""
Write a Python program to unpack a tuple in several variables.
"""
def unpack_tuple(input_tuple):
    a,b,c,d,e=tuple(each for each in input_tuple)
    return f'{a} {b} {c} {d} {e}'
if __name__ == "__main__":
    print(unpack_tuple(('BBA','BBS','CSIT','BE','BCOM')))