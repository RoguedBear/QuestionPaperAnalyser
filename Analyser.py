def analyser():
    # Beggining.

    print("-" * 60)
    print(f"{'Statistics of a Question Paper':^60s}")
    print("-" * 60)
    print()
    print("""Pre-requisites you must note before continuing:
    1) The question paper must be in a sorted order""")
    input("That's it!\nPress ENTER to continue\n")

    number_of_ch = int(input("Enter the number of chapters \n"))
    number_of_q = int(input("Enter Total Questions\n"))
    total_marx = int(input("Enter the total Marx of the paper.\n"))
    print()
    # --------------------
    # Main Dictionary

    main = {}

    # Creating nested dictionaries .
    for i in range(1, number_of_ch + 1):
        main[i] = {}
    # ----------------------------

    ch_index = []
    # Assigning names
    for a in range(1, number_of_ch + 1):
        print(f"Enter the name of chapter {a}")
        ch = input('')
        main[a]['name'] = ch
        ch_index.append(ch)

    # Assigning q's attempted
    for a in range(1, number_of_ch + 1):
        main[a]['q number'] = []
    # print(main)

    # main= {1: {'name':'Mole', 'questions':}}, [[1,2

    x = ''
    #    Pretty printing Chapterlist
    for n in range(1, len(ch_index) + 1):
        x += f"{n}. {ch_index[n - 1]}\n"

    # Formatting list
    L = []  # for recording number of questions in our paper
    for a in range(1, number_of_ch + 1):
        L.append([a, 0])
    # ------------------------

    # Recording chapter's question count and question number

    for b in range(1, number_of_q + 1):
        print(f'\n{x}')
        print(f"Question: {b}")
        ch = int(input("Enter Chapter NUMBER\n"))
        L[ch - 1][1] += 1
        main[ch]['q number'].append(b)
    # print(L)

    # Inserting that {number of question} into our dictionary.
    for a in range(1, number_of_ch + 1):
        main[a]['questions'] = L[a - 1][1]

    # print(main)
    # ----------------------------------------

    # Markx
    # Example: marks = {1: 1, ... , 20: 5}
    markx = {}

    # Asking marks group.
    y_marx = eval(input("\nHow many Markx groups. Example: [1,3,5]\n"))
    q_first = 1
    for a in range(len(y_marx)):
        q_marx = int(input(f"Enter the last question number for marks {y_marx[a]}. \t Previous question: {q_first}\n"))
        while q_first != (q_marx + 1):
            markx[q_first] = y_marx[a]
            q_first += 1
    # --------------------------------

    # Inserting key 'total marks' in each chapter
    for a in range(1, len(main) + 1):
        main[a]['total marks'] = 0
    # Revealing total marks of each chapter.
    for a in range(1, len(main) + 1):
        for b in range(len(main[a]['q number'])):
            main[a]['total marks'] += markx[main[a]['q number'][b]]

    # -----------------------------

    # Weightage.
    for a in range(1, len(main) + 1):
        main[a]['weightage'] = (main[a]['total marks'] / total_marx) * 100

    # -------------------------------
    return main


if __name__ == '__main__':
    analyser()