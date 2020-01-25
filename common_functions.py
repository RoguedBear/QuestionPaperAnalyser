# List of Common functions (because i just needed choice_prompt. Will add more functions if I restructure the program


def choice_prompt(prompt, *choices):
    """
    A Choice Prompt functions which will return the option-ed choice only
    :param prompt:  Input prompt
    :param choices: Any number of choice options
    :return:  Choice
    """
    while True:
        user_choice = input(f"\n{prompt}?\n> ")
        try:
            # print(f"Choice: {user_choice}\t List: {choices}")  # Debug Line
            if user_choice[0] in list(choices):
                return user_choice[0]

            else:
                print("Wrong choice. Try again...\n")
                continue
        except IndexError:
            print("Uhm... No! Try again...\n")
            continue


# Moved here, because no functions declaration in Main file
def ask_exit():
    """
    Asks the user whether they want to exit or not
    :return: None
    """
    print()
    print("-" * 60)
    print("Do you want to quit now?(Y/N)")
    yes_or_not = input()
    if yes_or_not[0].lower() == 'y':
        quit()
    else:
        print("-" * 60)
        print()
