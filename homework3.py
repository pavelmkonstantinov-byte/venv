import matplotlib.pyplot as plt


def main():
    x_values = [
        0,
        31.62278,
        89.44272,
        164.3168,
        252.9822,
        353.5534,
        464.758,
        585.662,
        715.5418,
        853.815,
        1000
    ]
    y_values = [
        0,
        0.43,
        1.12,
        2.07,
        3.15,
        4.34,
        5.63,
        7,
        8.44,
        10.22,
        11.96
    ]

    figure = plt.figure(figsize=(10, 6))
    axes = figure.add_subplot(1, 1, 1)

    axes.plot(
        x_values,
        y_values,
        marker="o",
        linestyle="-",
        color="royalblue",
        label="Значения из таблицы",
    )

    axes.set_xlim(0, 1000)
    axes.set_ylim(0, 13)
    axes.set_xticks(range(0, 1001, 100))
    axes.set_yticks(range(0, 14, 2))
    axes.set_xlabel("Значение X")
    axes.set_ylabel("Значение Y")
    axes.set_title("График зависимости Y от X")
    axes.grid(True, linestyle="--", linewidth=0.6, alpha=0.7)
    axes.legend(loc="upper left")

    figure.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()