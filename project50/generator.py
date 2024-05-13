import json


def sort_list(e):
    return e[2].lower()


def generate_diff(file1, file2):

    with (
        open(file1, 'r', encoding='utf-8') as f1,
        open(file2, 'r', encoding='utf-8') as f2,
    ):
        data1 = json.load(f1)
        data2 = json.load(f2)
    diff_file = {}
    data1_keys = data1.keys()
    data2_keys = data2.keys()

    for key in data1_keys:
        if key in data2_keys and data1[key] == data2[key]:
            diff_file[f'   {key}'] = data1[key]
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
        strings.append(f"{key}: {item}")
    result = ";\n ".join(sorted(strings, key=sort_list))
    return '{\n' + f'{result}' + '\n}'

print(generate_diff('file1.json', 'file2.json'))