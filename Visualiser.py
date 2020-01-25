import matplotlib.pyplot as plt
from common_functions import choice_prompt
import numpy
from time import sleep


def visualise(dictionary, title=''):
    """

    :param dictionary:  takes a dictionary
    :param title:   title
    :return:
    """

    print("-" * 60)
    print(f"{'Graphical Plots':^60s}")
    print("-" * 60)
    print(f"\nWhich visual representation would you like to see for {title}?")
    current_graphs = "1) Pie Chart: Weightage \n2) Line Plot: Chapter Wise Number of Questions\n"
    choice = choice_prompt(current_graphs, '1', '2')
    print()

    if choice == '1':
        print("Diplaying Pie Chart...")
        sleep(0.5)
        pie_chart(dictionary)

    if choice == '2':
        print("Displaying Line Plot...")
        sleep(0.5)
        line_plot(dictionary)


# First Pie Chart
def pie_chart(dictionary):
    """
    Plots a Pie Chart from the given dictionary
    :param dictionary: Dictionary
    :return: None
    """
    x = [dictionary[i]['weightage'] for i in range(1, len(dictionary) + 1)]
    labels = [dictionary[i]['name'] for i in range(1, len(dictionary) + 1)]
    plt.figure(figsize=(10, 10))
    wedge, texts, autotexts = plt.pie(x, labels=labels, autopct=lambda y: f'{y:.2f}%', shadow=True, )
    plt.legend(wedge, labels,
               title="Chapters",
               loc='upper right',
               bbox_to_anchor=(-0.4, 0., 0.5, 0.5),
               shadow=True
               )

    plt.setp(autotexts, size=8, weight="bold", color='w')
    plt.title("Weightage Of Each Chapter")
    plt.show()


# Number Of Questions Line Plot
def line_plot(dictionary):
    """
    Line Plotter to visualise Chapterwise Questions
    :param dictionary:
    :return:
    """

    x_axis = numpy.arange(1, len(dictionary) + 1, 1)

    y_axis = [dictionary[i]['questions'] for i in range(1, len(dictionary) + 1)]

    plt.figure(figsize=(10, 10))
    # Formatting the labels, axis as integers etc
    plt.xlabel("Chapters")
    plt.ylabel("Number of questions")
    plt.title("Number of Questions Chapter-Wise")
    plt.yticks(y_axis)
    plt.xticks(x_axis)
    for x, y in zip(x_axis, y_axis):
        print(x)
        plt.annotate(f"{dictionary[x]['name']}",
                     (x, y),
                     textcoords='offset pixels',
                     xytext=(x, y - 1),
                     ha='center',
                     )
    # plt.ylim(y_axis[-1]+1)
    plt.plot(x_axis, y_axis, 'go-')
    plt.show()


if __name__ == '__main__':
    sample_d = {
        1: {'name': 'Solutions', 'q number': [9, 16, 22], 'questions': 3, 'total marks': 4,
            'weightage': 5.714285714285714},
        2: {'name': 'ElectroChem', 'q number': [18, 19, 20, 35], 'questions': 4, 'total marks': 8,
            'weightage': 11.428571428571429},
        3: {'name': 'Kinetics', 'q number': [29], 'questions': 1, 'total marks': 3,
            'weightage': 4.285714285714286},
        4: {'name': 'Surface Chem', 'q number': [15, 33], 'questions': 2, 'total marks': 4,
            'weightage': 5.714285714285714},
        5: {'name': 'Metallurgy', 'q number': [1, 24, 30], 'questions': 3, 'total marks': 6,
            'weightage': 8.571428571428571},
        6: {'name': 'P-block', 'q number': [21, 32], 'questions': 2, 'total marks': 5,
            'weightage': 7.142857142857142},
        7: {'name': 'Coordination', 'q number': [7, 14, 26], 'questions': 3, 'total marks': 4,
            'weightage': 5.714285714285714},
        8: {'name': 'Organic(1,2,3,4)',
            'q number': [2, 3, 5, 6, 10, 11, 12, 13, 17, 23, 25, 27, 28, 31, 36, 37],
            'questions': 16, 'total marks': 31,
            'weightage': 44.285714285714285},
        9: {'name': 'Polymers', 'q number': [4, 8], 'questions': 2, 'total marks': 2,
            'weightage': 2.857142857142857},
        10: {'name': 'Chem In Everyday', 'q number': [34], 'questions': 1, 'total marks': 3,
             'weightage': 4.285714285714286}}
    visualise(sample_d)
