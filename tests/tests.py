word = "tree"
tupe = *word,
guess_list = ['e', 't', 'r']
my_list = list((set(tupe)))
print(tupe)
print(my_list)

for element in guess_list:
    if element in my_list:
        my_list.remove(element)

if len(my_list) == 0:
    my_tuple = tuple(set(tupe))
    my_list = list(my_tuple)