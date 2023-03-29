
def stats():
    import numpy as np
    from matplotlib import pyplot as plt
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig, axs = plt.subplots(1, 1)
    data = [" ", "Einfache VL", "Doppelte VL", "ArrayList"], ["addLast","n","n", 1], ["insertAfter","n","n","n"], ["delete","n","n","n"],["find", "n", "n", 1],["getFirstElem", 1,1,1], ["getLastElement", "n", "1", "1"], ["writeList", "n", "n", "n"], ["getLength", "n", "n", 1], ["index", "n", "n", "n"], ["clearlist", "n", "n", 1], ["copyList", "n", "n", "n* log(n)"], ["extend", "n", "1", "n"],["pop", "n", "n", 1], ["sortList", "n^2", "n^2", "n^2"]

  
    colors = ["orange","white","white","white"] 
    cols = []
    for i in range(15):
        cols.append(colors)
    cols[0] = ["white", "orange", "orange", "orange"]
    axs.axis('tight')
    axs.axis('off')
    the_table = axs.table(cellText=data, loc='center', cellColours=cols)
    plt.show()

    if __name__ == "__main__":
        print("Stats imported!")