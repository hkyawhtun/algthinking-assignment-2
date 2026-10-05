from datetime import datetime
from time import time,  perf_counter
from data_generator import gen_element, gen_push, gen_pop, write_to_file
from max_heap import MaxHeap
from competitor import Competitor
import random
import csv
from pathlib import Path

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

def save_results(filename, headers, rows):
    path = RESULTS_DIR / filename

    with open(path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f"Saved results to {path}")


def experiment_1_generate(size=10):
    data = []
    for _ in range(size):
        operation = gen_push()
        data.append(f"{operation[0]} {operation[1]}")
    data.insert(0, str(size))
    filename = f"experiment_1_{size}.txt"
    write_to_file(filename, data)

    return filename



""" def experiment_1_run(input_file):
    # read the file s1-s5
    # start a timer
    start_time = time()
    # run the max heap 
    # stop the timer
    end_time = time()
    time_taken = end_time - start_time
    # start the timer
    # run against competitor
    # stop the timer
    # write the results to output file or to screen
    pass # remove this line when code is setup  """


def experiment_1_run(input_file):

    with open(f"experiments/{input_file}", "r") as file:
        lines = file.readlines()

    # Skip first line because it is the number of operations
    operations = lines[1:]

    # ---------------- MaxHeap ----------------
    heap = MaxHeap()

    start = perf_counter()

    for line in operations:
        parts = line.strip().split()
        key = int(parts[1])
        heap.push(key)

    heap_time = perf_counter() - start


    # ---------------- Competitor ----------------
    competitor = Competitor()

    start = perf_counter()

    for line in operations:
        parts = line.strip().split()
        key = int(parts[1])
        competitor.push(key)

    competitor_time = perf_counter() - start


    print("MaxHeap:", heap_time)
    print("Competitor:", competitor_time)

    return heap_time, competitor_time


        # ----------------  experiment_2 --------------------


def experiment_2_generate(size, gettop_probability):
    data = []

    for _ in range(size):

        if random.random() < gettop_probability:
            data.append("3")
        else:
            operation = gen_push()
            data.append(f"{operation[0]} {operation[1]}")

    data.insert(0, str(size))

    percentage = gettop_probability * 100

    filename = f"experiment_2_gettop_{percentage}.txt"

    write_to_file(filename, data)

    return filename

# ----------------------------------------------------#

def experiment_2_run(input_file):

    with open(f"experiments/{input_file}", "r") as file:
        lines = file.readlines()[1:]

    # Convert file lines into operations before timing
    operations = []

    for line in lines:
        parts = line.strip().split()

        if parts[0] == "1":
            operations.append((1, int(parts[1])))
        elif parts[0] == "3":
            operations.append((3, None))


    # MaxHeap
    heap = MaxHeap()

    start = perf_counter()

    for operation, key in operations:

        if operation == 1:
            heap.push(key)

        elif operation == 3:
            heap.getTop()

    heap_time = perf_counter() - start


    # Competitor
    competitor = Competitor()

    start = perf_counter()

    for operation, key in operations:

        if operation == 1:
            competitor.push(key)

        elif operation == 3:
            competitor.getTop()

    competitor_time = perf_counter() - start


    print("MaxHeap:", heap_time)
    print("Competitor:", competitor_time)

    return heap_time, competitor_time


    # experiment_2_generate()
    # experiment_2_run()

# ------------------------------- End of experiment_2 ----------------------------

def experiment_3_generate(size, pop_probability):
    data = []

    for _ in range(size):

        if random.random() < pop_probability:
            data.append("2")
        else:
            operation = gen_push()
            data.append(f"{operation[0]} {operation[1]}")

    data.insert(0, str(size))

    percentage = pop_probability * 100
    filename = f"experiment_3_pop_{percentage}.txt"

    write_to_file(filename, data)

    return filename


def experiment_3_run(input_file):

    with open(f"experiments/{input_file}", "r") as file:
        lines = file.readlines()[1:]

    operations = []

    for line in lines:
        parts = line.strip().split()

        if parts[0] == "1":
            operations.append((1, int(parts[1])))
        elif parts[0] == "2":
            operations.append((2, None))


    # MaxHeap
    heap = MaxHeap()

    start = perf_counter()

    for operation, key in operations:
        if operation == 1:
            heap.push(key)
        elif operation == 2:
            heap.pop()

    heap_time = perf_counter() - start


    # Competitor
    competitor = Competitor()

    start = perf_counter()

    for operation, key in operations:
        if operation == 1:
            competitor.push(key)
        elif operation == 2:
            competitor.pop()

    competitor_time = perf_counter() - start


    print("MaxHeap:", heap_time)
    print("Competitor:", competitor_time)

    return heap_time, competitor_time

    # experiment_3_generate()
    # experiment_3_run()

#----------------- End of experiment_3 ----------------------------\
    # experiment_4_generate()
    # experiment_4_run()

def experiment_4_run(input_file):

    with open(f"experiments/{input_file}", "r") as file:
        lines = file.readlines()[1:]

    # Extract exactly the same keys from Experiment 1
    keys = []

    for line in lines:
        parts = line.strip().split()
        keys.append(int(parts[1]))


    # ---------------- Method 1: heapify ----------------

    heap1 = MaxHeap()

    start = perf_counter()

    heap1.heapify(keys, len(keys))

    heapify_time = perf_counter() - start


    # ---------------- Method 2: push one-by-one ----------------

    heap2 = MaxHeap()

    start = perf_counter()

    for key in keys:
        heap2.push(key)

    push_time = perf_counter() - start


    print("Heapify:", heapify_time)
    print("Push one-by-one:", push_time)

    return heapify_time, push_time
    
#------------------ End of experiment_4 ----------------------------

    # This code runs when you click "run Python file"
if __name__ == "__main__":


    probabilities = [
        0.001,
        0.005,
        0.01,
        0.05,
        0.10
    ]

    results = []

    for probability in probabilities:

        filename = experiment_3_generate(
            1_000_000,
            probability
        )

        heap_time, competitor_time = experiment_3_run(filename)

        percentage = probability * 100

        print(
            percentage,
            "Heap:", heap_time,
            "Competitor:", competitor_time
        )

        results.append([
            percentage,
            heap_time,
            competitor_time
        ])

    save_results(
        "experiment_3_results.csv",
        ["PopPercentage", "MaxHeap", "Competitor"],
        results
    )