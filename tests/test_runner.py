import subprocess
import csv
import time
import matplotlib.pyplot as plt
from src.manacher import Manacher
from src.dp_solution import Solution

def call_cpp_longest_palindrome(s):
    result = subprocess.run(['./brute_force'], input=s.encode(), capture_output=True)
    return result.stdout.decode().strip()

def call_manacher(s):
    return Manacher(s).process()

def run_test_case(func, input_str):
    start = time.perf_counter()
    results = func(input_str)
    elapsed = (time.perf_counter() - start) * 1000
    return results, elapsed

TEST_CASES = []

with open("test_cases.csv", newline='') as tests:
    reader = csv.reader(tests)
    for row in reader:
        TEST_CASES.append(row[1])

brute_time = []
dp_time = []
manacher_time = []

rows = [["Input", "Brute_Result", "Brute_Time(ms)", "Dp_Results", "Dp_Time(ms)" ,"Manacher_Result", "Manacher_Time(ms)"]]

for item in TEST_CASES:
    brute_result, brute_elapsed = run_test_case(call_cpp_longest_palindrome, item)
    manacher_result, manacher_elapsed = run_test_case(call_manacher, item)
    #dp_results, dp_elapsed = run_test_case(lil sis func, item)

    brute_time.append(brute_elapsed)
    #dp_time.append(dp_elapsed)
    manacher_time.append(manacher_elapsed)

    #rows.append([item, brute_result, brute_elapsed, dp_results, dp_elapsed, manacher_result, manacher_elapsed])

print(brute_time)
print(dp_time)
print(manacher_time)

with open("output_file.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

fig,ax = plt.subplots(1,3)

ax[0].scatter(TEST_CASES, brute_time)
ax[0].set_title("Brute Force")
# ax[1].scatter(TEST_CASES, dp_time)
# ax[1].set_title("DP")
ax[2].scatter(TEST_CASES, manacher_time)
ax[2].set_title("Manacher")

for i in range(3):
    ax[i].set_xlabel("Cases")
    ax[i].set_ylabel("Time(ms)")
    ax[i].tick_params(axis='x', rotation=90)

plt.tight_layout()
plt.show()

plt.scatter(TEST_CASES, manacher_time, color='blue', label='Manacher')
# plt.scatter(TEST_CASES, dp_time, color='green', label='DP')
plt.legend()

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()