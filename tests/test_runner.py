import subprocess
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import string
import random
from src.manacher import Manacher
from src.dp_solution import Solution
from src.brute_force import Brute_Force

# ------------------- Core Functions -------------------

def call_cpp_longest_palindrome(s):
    result = subprocess.run(['./brute_force'], input=s.encode(), capture_output=True)
    return result.stdout.decode().strip()

def run_alg(func, input_str):
    start = time.perf_counter()
    results = func(input_str)
    elapsed = (time.perf_counter() - start) * 1000
    return results, elapsed
def change_cases():
    TEST_CASES = pd.read_csv('tests/test_cases.csv', header=None, names=["id", "test"])
    new_cases=[('1k',''.join(random.choices(string.ascii_lowercase , k=1000))),
               ('5k',''.join(random.choices(string.ascii_lowercase , k=5000))),
               ('10k',''.join(random.choices(string.ascii_lowercase , k=10000))),
    ]
    new_df=pd.DataFrame(new_cases,columns=['id','test'])
    Intensified_cases=pd.concat([TEST_CASES,new_df],ignore_index=True)
    return Intensified_cases
def run_test_cases():
    test_cases=change_cases()
    results=[]

    brute = Brute_Force()
    manacher = Manacher()
    dp = Solution()

    for _, row in test_cases.iterrows():
        case = row['test']
        if not isinstance(case, str) or case.strip() == '':
            case = ''

        # brute_result, brute_elapsed = run_alg(call_cpp_longest_palindrome, case)
        brute_result, brute_elapsed = run_alg(brute.longest_palindrome, case)
        dp_result, dp_time = run_alg(dp.longestPalindrome, case)
        man_result, man_time = run_alg(manacher.process, case)

        results.append({
            'id': row['id'],
            'Input': case,
            'Brute_Result': brute_result,
            'Brute_Time(ms)': brute_elapsed,
            'Dp_Results':dp_result,
            'Dp_Time(ms)': dp_time,
            'Manacher_Result': man_result,
            'Manacher_Time(ms)':man_time
        })

    return results, pd.DataFrame(results)

def write_file(results_: pd.DataFrame,filename: str='result.csv'):
    results_.to_csv(filename, index=False)
    print(f'Results written to {filename}')

def plt_benchmark(results_):
    barwidth = 0.25
    fig, ax = plt.subplots(figsize=(14,8))

    brute = results_df['Brute_Time(ms)']
    dp = results_df['Dp_Time(ms)']
    man = results_df['Manacher_Time(ms)']

    x = np.arange(len(results_))

    ax.bar(x, brute, color='r', width=barwidth, edgecolor='grey', label='Brute Force')
    ax.bar(x + barwidth, dp, color='g', width=barwidth, edgecolor='grey', label='DP')
    ax.bar(x + barwidth*2, man, color='b', width=barwidth, edgecolor='grey', label='Manacher')

    plt.xlabel('Test Cases', fontweight ='bold', fontsize = 15)
    plt.ylabel('Run time (ms)', fontweight ='bold', fontsize = 15)
    plt.xticks(x + barwidth,results_df['Input'], rotation=90)
    ax.set_yscale('log')
    plt.legend()
    plt.tight_layout()
    plt.savefig('chart.png', dpi=300, bbox_inches='tight')
    plt.show()

# ------------------- Run Everything -------------------

if __name__ == "__main__":
    results, results_df = run_test_cases()
    write_file(results_df)
    plt_benchmark(results)