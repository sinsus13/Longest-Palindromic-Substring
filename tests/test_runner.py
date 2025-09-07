import subprocess
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
from src.manacher import Manacher
from src.dp_solution import Solution

def call_cpp_longest_palindrome(s):
    result = subprocess.run(['./brute_force'], input=s.encode(), capture_output=True)
    return result.stdout.decode().strip()

def run_alg(func, input_str):
    start = time.perf_counter()
    results = func(input_str)
    elapsed = (time.perf_counter() - start) * 1000
    return results, elapsed
 
def run_test_cases():
    TEST_CASES = pd.read_csv('test_cases.csv', header=None, names=["id", "test"])
    results=[]   
    for _, row in test_cases.iterrows():
        case = row['test']
        if not isinstance(case, str) or case.strip() == '':
            case = ''
    
        brute_result, brute_elapsed = run_test_case(call_cpp_longest_palindrome, item)
            
        start = time.perf_counter()
        dp_result = dp.longestPalindrome(case)
        end = time.perf_counter()
        dp_time = (end - start)*1000
    
        start1 = time.perf_counter()
        man_result = manacher.process(case)
        end1 = time.perf_counter()
        man_time = (end1 - start1)*1000
            
        results.append({
            'id': row['id'],
            'Input': case,
            'Brute_Result': brute_result,
            'Brute_Time(ms)':
            'Dp_Results':dp_result,
            'Dp_Time(ms)': dp_time,
            'Manacher_Result': man_result,
            'Manacher_Time(ms)':man_time 
        })

    return results,pd.DataFrame(results)

def write_file(results_:pd.DataFrame,filename: str='result.csv'):
    results_.to_csv(filename, index=False)
    print('Results written to', filename)
    
def plt_benchmark(rows):
    barwidth=0.1
    fig= plt.subplots(figsize=(12,8))
    br=[br_t for br_t in rows['Brute_Time(ms)']]
    dp=[dp_t fro dp_t in rows['Dp_Time(ms)']]
    man=[man_t for man_t in rows['Manacher_Time(ms)']]
    br1 = np.arange(len(br)) 
    br2 = [x + barWidth for x in br1] 
    br3 = [x + barWidth for x in br2]
    plt.bar(br1,br_t,color='r',width=barwidth,edgecolor='grey',label='Brute Force')
    plt.bar(br2,dp,color='g',width=barwidth,edgecolor='grey',label='Dp')
    plt.bar(br3,man,color='b',width=barwidth,edgecolor='grey',label='Manacher')
    plt.xlabel('Algorithm', fontweight ='bold', fontsize = 15) 
    plt.ylabel('Run time (ms)', fontweight ='bold', fontsize = 15) 
    plt.xticks([r + barWidth for r in range(len(br))], 
            [cs for cs in rows['Input'])
    plt.legend()
    plt.tight_layout()
    plt.savefig('chart.png', dpi=300, bbox_inches='tight')
    plt.show()
result,result_df=run_test_cases=run_test_cases()
write_file(result_df)
plt_benchmark(result)
