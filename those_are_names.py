"""
This programs gets list of first names and list of last names and return a list
of the full names.
if wanted it's passable to pass ana argument states what the wanted minimum length for a name
"""


def name(first_name, last_name):
    return f'{first_name} {last_name}'


def full_names(first_names_list, last_names_list, min_length=None):
    full_names_list = list(map(name, first_names_list, last_names_list))
    if min_length is not None:
        return list(filter(lambda full_name: len(full_name) > min_length, full_names_list))

    return full_names_list
