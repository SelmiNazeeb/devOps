def bubble_sort_dict_by_value(d):
    # Convert dictionary to a list of tuples (key, value)
    items = list(d.items())
    
    # Bubble sort based on the value
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            # Compare adjacent items by their value (items[j][1] is the value)
            if items[j][1] > items[j+1][1]:
                # Swap the entire tuple
                items[j], items[j+1] = items[j+1], items[j]
    
    # Convert the sorted list of tuples back to a dictionary
    sorted_dict = dict(items)
    return sorted_dict

d = {'apple': 10, 'banana': 5, 'cherry': 20, 'date': 15}
sorted_d = bubble_sort_dict_by_value(d)
print(sorted_d)
