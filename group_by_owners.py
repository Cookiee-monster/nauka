def group_by_owners(files):
    dict = files
    res = {}

    for key in dict:
        val = dict[key]
        short_list = []
        if val not in res:
            short_list.append(key)
            res[val] = short_list
        else:
            short_list = res[val]
            short_list.append(key)
            res[val] = short_list
    return res

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(group_by_owners(files))