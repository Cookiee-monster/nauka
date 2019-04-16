def unique_names(names1, names2):
    unique_names_list = []
    names_combined = names1 + names2
    for name in names_combined:
        if name not in unique_names_list:
            unique_names_list.append(name)

    return unique_names_list

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia