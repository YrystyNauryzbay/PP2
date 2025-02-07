def heads(head, legs):
    for i in range(head + 1): 
        if i * 2 + (head - i) * 4 == legs:
            return f"Chickens: {i}, Rabbits: {head - i}"

print(heads(35, 94))
