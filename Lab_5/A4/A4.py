def get_data(file_name):
    data  = []

    for line in open(file_name, 'r'):
        data.append(line.replace('\n', '').split('\t'))

        for seq in data:
            seq[2] = RLE_decode(seq[2])

    return data


def get_commands(file_name):
    commands = []

    for line in open(file_name, 'r'):
        commands.append(line.replace('\n', '').split('\t'))

    return commands


def RLE_decode(seq):
    decod_seq = ''

    for index, element in enumerate(seq):
        if element.isdigit():
            decod_seq += seq[index+1]*(int(element)-1)
        else:
            decod_seq += element

    return decod_seq


def search(seq):
    seq = RLE_decode(seq)

    result = (
        f"{com_num:03d}   search   {seq}\n"
        "organism\t\t\t\tprotein\n"
    )

    for index, subject in enumerate(data):
        if seq in subject[2]:
            result += data[index][1] + '\t\t' + data[index][0] + '\n'
            break
    else:
        result += "NOT FOUND\n"

    return(result)


def diff(protein_1, protein_2):
    seqs = []
    qt = 0
    diff = 0

    result = (
        f"{com_num:03d}   diff   {protein_1}   {protein_2}\n"
        "amino-acids difference:\n"
    )

    for seq in data:
        if protein_1 in seq[0] or protein_2 in seq[0]:
            seqs.append(seq[2])
            qt += 1
    if protein_1 == protein_2:
        result += '0\n'
    elif qt == 2 or protein_1:
        for index in range(min(len(seqs[0]), len(seqs[1]))):
            if seqs[0][index] != seqs[1][index]:
                diff += 1
        result += str(max(len(seqs[0]), len(seqs[1])) - min(len(seqs[0]), len(seqs[1])) + diff) + '\n'
    else:
        result += "MISSING: " + protein_1 + '\t' + protein_2 + '\n'# ДОДЕЛАТЬ УТОЧНЕНИЕ КАКОЙ БЕЛОК НЕ НАЙДЕН

    return(result)


def mode(protein):

    result = (
        f"{com_num:03d}   mod   {protein}\n"
        "amino-acid occurs:\n"
    )

    for object in data:
        if protein in object[0]:
            seq = object[2]

    elements = {}
    for elem in seq:
        elements[elem] = elements.get(elem, 0) + 1

    max_qt = max(elements.values())

    max_elements = [elem for elem, index in elements.items() if index == max_qt]
    max_elements.sort()

    result += max_elements[0] + "          " + str(max_qt) + '\n'

    return result


data_file_name = "sequences.0.txt"
command_file_name = "commands.0.txt"
result_file_name = "genedata.0.txt"
SEP = "-------------------------------------------------------------------------"
data = get_data(data_file_name)
commands = get_commands(command_file_name)
com_num = 1


with open(result_file_name, 'w') as file:
    file.write("Gorbarchuk Alexander\n"
               "Genetic Searching\n"
               f"{SEP}\n"
               )

with open(result_file_name, 'a') as file:
    for command in commands:
        if command [0] == "search":
            file.write(search(command[1]))
        elif command [0] == "diff":
            file.write(diff(command[1], command[2]))
        elif command [0] == "mode":
            file.write(mode(command[1]))

        file.write(SEP + '\n')

        com_num += 1
