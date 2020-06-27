"""
Write a Python program to slice a tuple.
"""
def slice_tuple(input_tuple):
    list_convert = list(input_tuple)
    sliced =list_convert[1:3]
    return(tuple(sliced))

if __name__ == "__main__":
    print(slice_tuple(('BBA','BBS','CSIT','BE','BCOM')))