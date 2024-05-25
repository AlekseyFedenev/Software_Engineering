def get_employee_sequence(sequence, element):
    if element not in sequence:
        return tuple()

    start_index = sequence.index(element)
    end_index = sequence.index(element, start_index + 1) + 1

    return sequence[start_index:end_index]


input_sequence = (1, 8, 6, 9, 7, 8, 5, 4, 3)
input_element = 8

result_sequence = get_employee_sequence(input_sequence, input_element)
print(result_sequence)