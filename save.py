import os
from json import dump


def save(dictionary):
    """
    Saves the current dictionary to a JSON file
    :param dictionary: Dictionary
    :return: title
    """
    # Getting file name
    file_name = input("What should the be the name of the file?\n")
    # Working out the file path.
    cwd = os.getcwd()
    # print('Current working directory:', cwd)  # Debug
    if not os.path.exists('Saved'):
        os.mkdir('Saved')
    path = cwd + '/Saved/' + file_name + str('.json')  # str('.txt')
    # print("final directory:", path)  # Debug
    with open(path, 'w') as file:
        # Writing process.
        # file.write(str(file_name) + '\n')
        # file.write(str(dictionary) + '\n')
        # file.write(str(marks))

        # Writing process json
        dump(dictionary, file, indent=4)
        print(f"File saved to path: {path}")
    return file_name