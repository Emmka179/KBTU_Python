def unique_el(list_el):
    elements = []
    for item in list_el:
        if item not in elements:
            elements.append(item)
    return elements

list_el = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("List with unique elements:", unique_el(list_el))