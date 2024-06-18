import json
from project50.cli import open_filer


def sort_list(e):
    return e[2].lower()


def generate_diff(file1, file2):
    data1 = open_filer(file1)
    data2 = open_filer(file2)
    diff_file = {}
    data1_keys = data1.keys()
    data2_keys = data2.keys()

    for key in data1_keys:
        if key in data2_keys and data1[key] == data2[key]:
            diff_file[f'  {key}'] = data1[key]
        elif key in data2_keys and data1[key] != data2[key]:
            diff_file[f'- {key}'] = data1[key]
            diff_file[f'+ {key}'] = data2[key]
        elif key in data1_keys and key not in data2_keys:
            diff_file[f'- {key}'] = data1[key]

    for key2 in data2_keys:
        if key2 not in data1_keys and key2 in data2_keys:
            diff_file[f'+ {key2}'] = data2[key2]

    strings = []
    for key, item in diff_file.items():
        if item == True:
            strings.append(f"{key}: true")
        elif item == False:
            strings.append(f"{key}: false")
        else:
            strings.append(f"{key}: {item}")

    print(strings)

    result = "\n  ".join(sorted(strings, key=sort_list))
    return '{\n  ' + f'{result}' + '\n}'


