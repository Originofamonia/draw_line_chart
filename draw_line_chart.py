import matplotlib.pyplot as plt
import numpy as np


# read in jsim output file and return an array
def read_out_file(filename):
    with open(filename) as textFile:
        lines = [line.split() for line in textFile]

    new_lines = list(map(list, zip(*lines)))
    data = [[float(y) for y in x] for x in new_lines]
    return data


def draw_line_chart(data):
    for index in range(len(data)):
        if index == 0:
            continue
        plt.subplot(len(data) - 1, 1, index)
        plt.plot(data[0], data[index], c=np.random.rand(3,))
        plt.xlabel(index)
        plt.grid()

    plt.show()


def demo_draw_line_chart():
    year = [1960, 1970, 1980, 1990, 2000, 2010]
    pop_pakistan = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6]
    pop_india = [449.48, 553.57, 696.783, 870.133, 1000.4, 1309.1]
    plt.plot(year, pop_pakistan, color='g')
    plt.plot(year, pop_india, color='orange')
    plt.xlabel('Countries')
    plt.ylabel('Population in million')
    plt.title('Pakistan India Population till 2010')
    plt.grid()
    plt.show()


def main():
    filename = 'SPLITTER_OUT'
    data = read_out_file(filename)
    draw_line_chart(data)
    # demo_draw_line_chart()


if __name__ == '__main__':
    main()
