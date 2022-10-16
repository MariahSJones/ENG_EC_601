import os

__all__ = ["check_empty_str_in_dict", "json_check", "masked_dict_vals"]

# checks each key:value in dictionary for empty strings
def check_empty_str_in_dict(input_dictionary):
    for key, value in input_dictionary.items():
        if value in ["", "None"]:
            raise ValueError(f"the value of {key} is {value}")
    return


# check if file exists and can be read
def json_check(file_name):
    if os.path.isfile(file_name) and os.access(file_name, os.R_OK):
        print(f"The file exists, and is readable! \n")
    else:
        raise FileNotFoundError(f"{file_name} is missing or is not readable!")


# masks dictionary values
def masked_dict_vals(input_dictionary, list_not_to_mask=[]):

    # make a copy of the dictionary
    output_dictionary = input_dictionary.copy()

    # iterate through the dictionary
    for key in input_dictionary.keys():
        if key in list_not_to_mask:
            pass
        else:
            # replace with asterisks
            output_dictionary[key] = len(input_dictionary[key]) * "*"
    return output_dictionary
