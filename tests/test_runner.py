import subprocess
import csv
import time

def call_cpp_longest_palindrome(s):
    result = subprocess.run(['./brute_force'], input=s.encode(), capture_output=True)
    return result.stdout.decode().strip()

def run_test_case(func, input_str):
    start = time.perf_counter()
    func(input_str)
    elapsed = (time.perf_counter() - start) * 1000
    return elapsed

TEST_CASES = []

with open("test_cases.csv", newline='') as tests:
    reader = csv.reader(tests)
    for row in reader:
        TEST_CASES.append(row[1])

brute_time = []
dp_time = []

for items in TEST_CASES:
    brute_time.append(run_test_case(call_cpp_longest_palindrome, items))
    #dp_time.append(run_test_case(lil_sis_dp_func, item))

print(brute_time)
