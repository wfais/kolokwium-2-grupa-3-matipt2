import numpy as np
import matplotlib.pyplot as plt


def draw_scatter_plot():
    """
    1) Wygeneruj dane x, y (np. np.arange(10) i jakieś y losowe).
    2) Rysuj wykres punktowy (scatter).
    3) Ustaw etykiety osi, tytuł, legendę.
    4) Zwróć obiekt Figure.
    """
    np.random.seed(123)

    x = np.arange(10)
    y = np.random.rand(10)

    fig, ax = plt.subplots()

    ax.scatter(x, y, label='Punkty danych')

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_title('Wykres punktowy')

    ax.legend()

    return fig


if _name_ == '_main_':
    fig = draw_scatter_plot()
    plt.show()