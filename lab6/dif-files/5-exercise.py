def write_list_to_file(filename, elements):
    with open(filename, 'a') as f:
        f.write(" ".join(map(str, elements)) + "\n")

write_list_to_file("sometext.txt", [12345, 56789, 90987654, "dfghjkl", "efrgf", 34, 34])
