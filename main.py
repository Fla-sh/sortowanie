import algorithms
import list_generator
import tests
from plotting import plotting

if __name__ == "__main__":

    algorithms_list = [
        # algorithms.insertion_sort,
        # algorithms.selection_sort,
        # algorithms.heap_sort,
        algorithms.shell_sort,
        # algorithms.quick_sort_left,
        # algorithms.quick_sort_right,
        # algorithms.quick_sort_middle,
        # algorithms.quick_sort_random,
        # algorithms.heap_sort
    ]

    for algorithm in algorithms_list:
        try:
            tests.Test(algorithm)
        except Exception as e:
            print(e)
            continue

    for algorithm in algorithms_list:
        plotting.Plotting(algorithm).plot()

