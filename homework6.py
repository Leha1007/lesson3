

def calculate_structure_sum(data_structure):
    s = 0
    x = str(data_structure)
    my_chars = ['[', ']', '{', '}', '(', ')', ',', ':', "'"]
    for ch in my_chars:
        x = x.replace(ch, ' ')
    for n in x.split():
        try:
            s += int(n)
        except ValueError:
            s += len(n)
    return s


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(calculate_structure_sum(data_structure))
