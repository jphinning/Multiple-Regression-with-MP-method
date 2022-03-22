import matplotlib.pyplot as plt


def get_scattered_chart(input, output, c_title='Data', c_label='data'):
    # Ploting charts
    fig, ax = plt.subplots()

    plt.plot(input, output, 'o',
             label=c_label, markersize=0.5)
    ax.set(xlabel='input', ylabel='output', title=c_title)
    plt.legend()
    ax.grid()

    fig.savefig(f"{c_title}.png")
