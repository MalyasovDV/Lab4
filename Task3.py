def list_without_copies(sequence):
    result_list = []
    for number in sequence:
        try:
            result_list.index(number)
        except:
            result_list.append(number)
    return result_list


sequence = [1, 4, 5, 1, 2, 10, 10, 10, 20, 4, 6, 2]

print(list_without_copies(sequence))