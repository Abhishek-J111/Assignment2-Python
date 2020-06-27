"""
Write a Python program to remove a key from a dictionary.
"""
def remove_key(input_dict,key):
    if key in input_dict:
        print(f'Removing key {key}')
        input_dict.pop(key)
        return input_dict
    return f'no key to delete'
        
if __name__ == "__main__":
    inputKey=int(input("Enter integer key"))
    print(remove_key({1:10, 2:20, 3:30, 4:40, 5:50},inputKey))