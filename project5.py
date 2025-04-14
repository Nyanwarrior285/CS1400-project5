'''
data set found at:
https://catalog.data.gov/dataset/california-power-plants-b4c40/resource/c75831fc-3d6c-4754-8e4a-c49007bd27f7
'''
import matplotlib.pyplot as plt


def get_data():
    data = open("data.csv")
    dataset = []
    for line in data:
        line = line.strip()
        '''
        After messing around for a bit trying to get things to work, I realized that
        the data format includes some names that sometimes have commas in them, which
        messes things up if you're only spliting on commas, but they're always
        surrounded by quotation marks, so this is my attempt at getting it to work
        '''
        if '"' in line:
            line_data = line
            line_part = []
            while '"' in line_data:
                index1 = line_data.find('"')
                index2 = index1 + 1 + line_data[index1+1:].find('"')
                line_part += line_data[:index1-1].split(",") + [line_data[index1+1:index2]]
                line_data = line_data[index2+2:]
            line_data = line_part + line_data.split(",")
        else:
            line_data = line.split(",")
        dataset.append(line_data)
    data.close()
    return dataset


def create_graph(data):
    plt.ylabel("Megawatts Production")
    plt.xlabel("Power Plant")
    power = []
    for line in data[1:]:
        if line[6]:
            power += [float(line[6])]
        else:
            pass
    print(min(power))
    print(max(power))
    print(len(power))
    plt.bar(range(len(power)),power)
    plt.title("Different power plants in California and their maximum power output")
    plt.show()


def main():
    data = get_data()
    create_graph(data)


if __name__ == "__main__":
    main()
