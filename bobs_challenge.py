from itertools import combinations

MOD = 10**9 + 7

def read_input():
    print("Enter number of test cases:")
    t = int(input())
    test_cases = []
    for _ in range(t):
        print("Enter n and k:")
        n, k = map(int, input().split())
        print("Enter array:")
        arr = list(map(int, input().split()))
        test_cases.append((n, k, arr))
    return test_cases

def process_data(test_cases):
    results = []
    for n, k, arr in test_cases:
        medians = []
        for comb in combinations(arr, k):
            sorted_comb = sorted(comb)
            median = sorted_comb[k // 2]
            medians.append(median)
        results.append(sum(medians) % MOD)
    return results

def print_result(results):
    for res in results:
        print(res)

if __name__ == "__main__":
    test_cases = read_input()
    results = process_data(test_cases)
    print_result(results)
