import matplotlib.pyplot as plt
import csv
from pprint import pprint

def check_header(firstLine:list):
    """
    Check if first line is a header.

    Parameters
    ----------
    firstLine:list -> first line of csv-file
    """
    for elem in firstLine:
        for letter in elem:
            if letter.isalpha():
                return True
    return False

def read_csv(file_path):
    x:list = [] # x-data (Elements)
    yOwn:list = [] # y-data for own implementation (Runtime in ns)
    yStd:list = [] # y-data for standard implementation (Runtime in ns)

    with open(file_path, 'r') as file:
        reader = csv.reader(file) # read csv-file
        header = next(reader)
        data = [] # data list
        if not check_header(header): # if first line is no header
            data.append(header) # append header to data list
        for row in reader: # iterate over rows
            x.append(int(row[0])) # append x-data
            yOwn.append(int(row[1])) # append y-data for own implementation
            yStd.append(int(row[2])) # append y-data for standard implementation
            data.append(row) # append row to data list
    return x, yOwn, yStd, header, data

def plot_runtime(x:list, yOwn:list, yStd:list, header:list, funcName:str, xAccuracy:str="ns"):
    plt.plot(x, yOwn, label=header[1]) # plot own implementation
    plt.plot(x, yStd, label=header[2]) # plot standard implementation
    plt.title(f"{funcName} - {header[1]} vs. {header[2]}") # title
    plt.xlabel('Anzahl Elemente') # x-axis label
    plt.ylabel(f'Laufzeit ({xAccuracy})') # y-axis label
    plt.legend() # legend
    return plt

if __name__ == '__main__':
    # ### Beispiel fuer eine Datei in einem Plot ###
    # # removeFront
    # x, yOwn, yStd, header, data = read_csv('listRemoveFrontRuntimeTest.csv')
    # plot = plot_runtime(x, yOwn, yStd, header, "removeFront()")
    # plot.savefig("removeFront.png")
    # plot.show()

    # ### Beispiel fuer 2 Dateien in einem Plot ###
    # # insertAfter
    # x, yOwn, yStd, header, data = read_csv('dListInsertAfterRuntimeTest.csv')
    # plot_runtime(x, yOwn, yStd, header, "insertAfter()")
    # x, yOwn, yStd, header, data = read_csv('listInsertAfterRuntimeTest.csv')
    # plot = plot_runtime(x, yOwn, yStd, header, "insertAfter()")
    # plot.savefig("insertAfter.png")
    # plot.show()

    pass

