def find_it(seq):
    for number in set(seq):
        if seq.count(number) % 2 != 0:
            return number
    return None