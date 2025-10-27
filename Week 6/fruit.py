
def reverse(fruit_list):
    new_fruit_list=["","","",""]
    length = len(fruit_list)
    for i in  range (0, length):
        new_fruit_list[i] = fruit_list[length -(i+1)]
    fruit_list = new_fruit_list
    return fruit_list

def find_val(val, fruit_list):
    try: 
        index=fruit_list.index(val)
    except ValueError: 
        print(f'The value "{val}" is not in the list')
    return index


def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list=reverse(fruit_list)    
    print(f"reversed: {fruit_list}")
    fruit_list.append("orange")
    print(f"append orange: {fruit_list}")
    fruit_list.insert(find_val("apple", fruit_list), "cherry")
    print(f"insert cherry: {fruit_list}")
    fruit_list.remove("banana")
    print(f"remove banana: {fruit_list}")
    print(f"pop {fruit_list.pop()}: {fruit_list}")
    fruit_list.sort()
    print(f"sorted: {fruit_list}")
    fruit_list.clear()
    print(f"cleared: {fruit_list}")

if __name__=="__main__": 
    main()