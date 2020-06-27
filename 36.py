"""
Write a Python program to sum all the items in a dictionary.
"""
def sum_dict(input_dict):
    return sum(input_dict.values())
        
if __name__ == "__main__":
    print(sum_dict({1:10, 2:20, 3:30, 4:40, 5:50}))