import os

__all__ = ["check_empty_str_in_dict", "json_check", "masked_dict_vals"]


def check_empty_str_in_dict(input_dictionary):
    """
    checks each key:value in dictionary for empty strings
    """
    for key, value in input_dictionary.items():
        if value in ["", "None"]:
            raise ValueError(f"the value of {key} is {value}")
    return


def json_check(file_name, verbose=False):
    """
    check if file exists and can be read
    """
    if not os.path.isfile(file_name) or not os.access(file_name, os.R_OK):
        raise FileNotFoundError(f"{file_name} is missing or is not readable!")
    if verbose:
        print(f"The {file_name} exists, and is readable! \n")


def masked_dict_vals(input_dictionary, list_not_to_mask=None):
    """
    masks private dictionary values
    """
    if list_not_to_mask is None:
        list_not_to_mask = []
    # make a copy of the dictionary
    output_dictionary = input_dictionary.copy()

    # iterate through the dictionary
    for key in input_dictionary.keys():
        if key not in list_not_to_mask:
            # replace with asterisks
            output_dictionary[key] = len(input_dictionary[key]) * "*"
    return output_dictionary
