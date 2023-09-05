from csv import reader
from math import sqrt
from random import seed
from random import randrange

# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            #print(row)
            if not row:
                continue
            dataset.append(row)
    return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

# Find the min and max values for each column
def dataset_minmax(dataset):
    minmax = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])
    return minmax

# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

# calculate column means
def column_means(dataset):
    means = [0 for i in range(len(dataset[0]))]
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        means[i] = sum(col_values) / float(len(dataset))
    return means

# calculate column standard deviations
def column_stdevs(dataset, means):
    stdevs = [0 for i in range(len(dataset[0]))]
    for i in range(len(dataset[0])):
        variance = [pow(row[i]-means[i], 2) for row in dataset]
        stdevs[i] = sum(variance)
        stdevs = [sqrt(x/(float(len(dataset)-1))) for x in stdevs]
    return stdevs

# standardize dataset
def standardize_dataset(dataset, means, stdevs):
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - means[i]) / stdevs[i]

# Split a dataset into a train and test set
def train_test_split(dataset, split=0.60):
    train = list()
    train_size = split * len(dataset)
    dataset_copy = list(dataset)
    while len(train) < train_size:
        index = randrange(len(dataset_copy))
        train.append(dataset_copy.pop(index))
    return train, dataset_copy

##Ejercicios
def print_cols_first_ten_rows(dataset):
    i = 0
    while i < 10:
        print(dataset[i])
        i += 1

def main():
    dataset = load_csv("./wine.csv")
    #Ej 3
    for i in range(0, 14):
        str_column_to_float(dataset, i)

    #Ej 2
    print("10 priemras filas")
    print_cols_first_ten_rows(dataset)

    #Ej 4
    res_min_max = dataset_minmax(dataset)
    print("\nValores minimos y maximos de cada columna")
    print(res_min_max)

    #Ej 5
    means = column_means(dataset)
    print("\n Las medias de cada columna")
    print(means)

    #Ej 6
    stdevs = column_stdevs(dataset, means)
    print("\n Desviación estándar")
    print(stdevs)

    #Ej 7
    normalize_dataset(dataset, res_min_max)
    
    #Ej 8
    standardize_dataset(dataset, means, stdevs)

    #Ej 9
    train, test = train_test_split(dataset)
    print("\nLa data de entrenamiento\n")
    print(train)
    print("\nLa data de test\n")
    print(test)
main()  