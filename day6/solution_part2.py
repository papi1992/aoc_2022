distinct_chars = 14

with open("input.txt") as buffer:
    data = buffer.read()
    for i in range(len(data)):
        start_index, end_index = 0 + i, distinct_chars + i
        if len(set(data[start_index: end_index])) == distinct_chars:
            print(i  + distinct_chars)
            break
