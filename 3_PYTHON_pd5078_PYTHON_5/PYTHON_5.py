DNA_seq = "ATGAAAAAAATCTGAGCTGCTC"

print(DNA_seq, type(DNA_seq))

DNA_seq_list = list(DNA_seq)

print(DNA_seq_list)

# wyświetlenie nukleotydów sekwencji po kolei
for i in range(len(DNA_seq_list)):
    print(DNA_seq_list[i])