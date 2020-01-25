from time import sleep

# Initialising / Importing functions
import Analyser
from table import table
from save import save
from load_json import loaddict
from Visualiser import visualise
from common_functions import choice_prompt, ask_exit

print("=" * 60)
print(f"{'Question Paper Analyser':~^60}")
print("=" * 60)
print()
print(f"{'Welcome to Question Paper Analyser !':^60}")
quit_ = 'no'  # To differentiate between python's quit() and the chosen variable

prev_file = ''  # Variable (tuple) which will store previously accessed files
analysed_dictionary = ''  # Initialising Variables
title = ''  # Initialising Variables
# Project Loop starts.
while quit_ == 'no':
    print("""What would you like to do?
    1) Analyse a Question Paper
    2) Display the weightage of of any previously saved Question Paper
    3) Visualise data Graphically""")

    choice = input("Enter Choice...\t")

    # 1) Analysing The Question paper
    if choice == '1':
        print("\nOkay, Starting Analyser...\n")
        sleep(0.5)
        analysed_dictionary = Analyser.analyser()
        print('-'*30)
        # print(f"dictionary, {analysed_dictionary}")  # Debug

        # Prompt to view the weightage table
        triv_choice = choice_prompt("Do you want to view the weightage table?", 'y', 'n')
        if triv_choice == 'y':
            print("\nOkay, here's the weightage table:")
            sleep(0.5)
            table(analysed_dictionary)
        else:
            print("Ok")

        # Saving.
        triv_choice = choice_prompt("Do you want to save the current dictionary?", 'y', 'n')
        if triv_choice == 'y':
            print("Okay, starting Save module...")
            print('-' * 30)
            sleep(0.5)
            print()
            title = save(analysed_dictionary)
        else:
            print("k")
            title = ''

        prev_file = (analysed_dictionary, title)
        ask_exit()

    if choice == '2':
        print("Ok...\n")
        sleep(0.5)

        # If user wants to use the previously scanned file
        if prev_file:  # If previous file is not empty
            print('-'*30)
            choice = choice_prompt(f"Do you want to use the previous file: {prev_file[1]}", 'y', 'n')
            if choice == 'y':
                analysed_dictionary, title = prev_file
            if choice == 'n':
                analysed_dictionary, title = loaddict()
            print('-'*30)
        else:
            # Getting the dictionary (and the title) from the saved file
            prev_file = loaddict()
            analysed_dictionary, title = prev_file

        print("Done! Here is your table:")
        sleep(0.5)
        table(analysed_dictionary, title)

        ask_exit()

    if choice == '3':

        if prev_file:  # If the previous file is not empty
            choice = choice_prompt(f"Do you want to use the previous file: {prev_file[1]}", 'y', 'n')
            if choice == 'y':
                analysed_dictionary, title = prev_file
            if choice == 'n':
                analysed_dictionary, title = loaddict()
        else:
            # Getting the dictionary (and the title) from the saved file
            analysed_dictionary, title = loaddict()
            prev_file = (analysed_dictionary, title)

        visualise(analysed_dictionary, title)

        ask_exit()
