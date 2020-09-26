items = [(1,2,3),(4,5,6),(7,8,9),(2,4,6),(8,9,10)]
letters = ['a','b','c','d']
numbers = ['a',123,'b',456,'c',789]
items_row = [1,2,3,4,5,6,7,8, 9,10,11,12,13,14,15,16,17,18,19,20]
even_items = []
user1 = ['Elon Musk',32,'Unemployed','Single']
user2 = ['Bernie Sanders',31,'Employed','Single']

#print all the different ordered pairs
def print_all_possible_ordered_pairs(items):
    for first_item in items:
        for second_item in items:
            for third_item in items:
                print(first_item,second_item,third_item)
#print all the first items
def print_all_first_items(items):
    first_item = items[0]
    text_for_print(first_item)
#sort the list and then print the last item
def print_last_item(items):
    sorted_items = sorted(items)
    last_item = sorted_items[-1]
    text_for_print(last_item)
#print all the even numbers in the list passed in
def print_all_even_numbers(items):
    for item in items:
        if (item % 2) == 0:
            even_items.append(item)
        else:
            pass
#take the result and print with text The answer is
def text_for_print(items):
    what = ("The answer is :")
    print(what)
    print(items)
#Print the name of the person
def print_name(items):
    name = items[0]
    print(name)
#Print the age of the person
def print_age(items):
    age = items[1]
    print(age)
#Print the employment status of the person
def print_employment_status(items):
    status = items[2]
    print(status)
#Print the marital status of the person
def print_marital_status(items):
    relationship = items[3]
    print(relationship)

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False

print_all_possible_ordered_pairs(items)
print_all_first_items(letters)
print_all_even_numbers(items_row)
print_name(user1)
print_age(user1)
print_employment_status(user1)
print_marital_status(user1)
monkey_trouble(True, False)
