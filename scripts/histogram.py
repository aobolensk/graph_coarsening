import sys
import matplotlib.pyplot as plt

file = sys.argv[1]

if __name__ == "__main__":
    f = open(file)
    x = []
    num_bins = 500
    for index, line in enumerate(f):
        data = line.split()
        x.append(float(data[-1]))
        if (index < 50):
            print(float(data[-1]))
    plt.hist(x, bins=num_bins)
    print("min: ", min(*x))
    print("max: ", max(*x))
    plt.show()
