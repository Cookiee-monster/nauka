import time

start = time.time()


def check_step(sequence, grid_size):
    """

    :param sequence: set of already founded paths
    :param grid_size: size of the network
    :return: new sequence of paths, one step longer
    """

    new_sequences = []

    # Step to the East is only possible if path contain more steps to North then to the East
    if sequence.count("E") < sequence.count("N"):
        new_sequences.append(sequence + "E")

    # Number of steps to the North has to be equal or smaller than grid size
    if sequence.count("N") < grid_size:
        new_sequences.append(sequence + "N")

    if new_sequences:
        return new_sequences


def enumerate_paths(grid_size):

    paths_sequence = ["N"]

    iteration = 1
    while iteration < 2*grid_size: # iteration is expanding set of paths with one step to the north or east

        number_of_sequence = len(paths_sequence)
        i = 0
        iteration_start = time.time()
        while i < number_of_sequence:

            paths_sequence += check_step(paths_sequence.pop(0), grid_size)
            i += 1
        iteration += 1
        iteration_stop = time.time()
        print("Iteration {} computing time {} ".format(iteration, iteration_stop-iteration_start))

    print("All possible paths - N means step to North, E means step to East")
    print(paths_sequence)

    stop = time.time()

    print("Total time {} for {} paths".format(str(stop - start), str(len(paths_sequence))))


enumerate_paths(11)
