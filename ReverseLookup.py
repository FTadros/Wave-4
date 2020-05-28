key = ''
key_list = []
value_list = []
final_list = []


def reverseLookup(dictionary, value):
    for x, y in dictionary.items():
        if y == value:
            final_list.append(x)
            return final_list

while key != '##':
    key = input("Please enter a key (input ## to stop): ")
    key_list.append(key)

i = len(key_list)

while i > 1:
    value = input("Please enter a value: ")
    value_list.append(value)
    i -= 1

my_dict = dict(zip(key_list, value_list))

user_input = input('What value would you like to search for? ')

print(reverseLookup(my_dict, user_input))
