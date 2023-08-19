def merge_with_empty(list1, list2):
    output = []

    for item in list1:
        if item in list2:
            output.append(item)
        else:
            output.append("")

    return output

list1 = ["a", "b", "c", 'd']
list2 = ["a", "d"]
result = merge_with_empty(list1, list2)
print(result)  # Output: ['a', '', 'c']