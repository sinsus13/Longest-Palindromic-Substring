# Longest Palindromic Substring
**Converted from** `Longest Palindromic Substring.docx` by Sina Rajabi & Raya Faezinia. fileciteturn0file0

---

## Table of Contents
1. [Problem](#problem)  
2. [Examples](#examples)  
3. [Solution Approaches](#solution-approaches)  
   - [Dynamic Programming (Python)](#dynamic-programming-python)  
   - [Brute-Force (C++)](#brute-force-c)  
   - [Expand Around Center (optional, Python)](#expand-around-center-optional-python)  
4. [Complexity Analysis](#complexity-analysis)  
5. [Mathematical Note: Number of Substrings](#mathematical-note-number-of-substrings)  
6. [Conclusion](#conclusion)  
7. [Sources](#sources)  

---

## Problem
A **palindrome** is a string that reads the same forwards and backwards (e.g. `racecar`).  
**Given** a string `s`, **find the longest palindromic substring** inside `s`.  
**Example:** for `s = "dsadasjh"`, the longest palindromic substring is `"sadas"`. (Source document: Sina Rajabi & Raya Faezinia). fileciteturn0file0

---

## Examples
```text
Input:  "babad"
Output: "bab"   # or "aba"

Input:  "cbbd"
Output: "bb"

Input:  "abssbm"
Output: "bssb"  # as explained in the source document example. fileciteturn0file0
```

---

## Solution Approaches

### Dynamic Programming (Python)
This approach fills an `n x n` boolean table `dp[i][j]` where `dp[i][j] == True` means `s[i..j]` is a palindrome. We build the table from shorter substrings up to longer substrings (diagonal-by-diagonal).

**Properties:**
- `dp[i][i] = True` (single characters are palindromes).
- For length `L >= 2`, `dp[i][j] = (s[i] == s[j]) and (L == 2 or dp[i+1][j-1])`.

**Complexities:** Time = `O(n^2)`, Space = `O(n^2)`.

**Python implementation (working):**
```python
def longest_palindromic_substring_dp(s: str) -> str:
    if not s:
        return ""
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1

    # All substrings of length 1 are palindrome
    for i in range(n):
        dp[i][i] = True

    # Check substrings of length L = 2..n
    for L in range(2, n + 1):
        for i in range(0, n - L + 1):
            j = i + L - 1
            if s[i] == s[j]:
                if L == 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if L > max_len:
                        start = i
                        max_len = L

    return s[start:start + max_len]

# Example usage:
if __name__ == "__main__":
    tests = ["babad", "cbbd", "abssbm", "dsadasjh", ""]
    for t in tests:
        print(f"{t!r} -> {longest_palindromic_substring_dp(t)!r}")
```

---

### Brute-Force (C++)
A straightforward brute-force method checks every possible substring starting from the longest substrings to the shortest; once a palindromic substring is found we return it. This yields worst-case time complexity `O(n^3)` (two loops to choose substring + linear check).

**C++ implementation (working):**
```cpp
#include <bits/stdc++.h>
using namespace std;

string longestPalindromeBrute(const string &s) {
    int n = (int)s.size();
    if (n == 0) return "";

    // Check substrings by decreasing length
    for (int len = n; len >= 1; --len) {
        for (int i = 0; i + len <= n; ++i) {
            int l = i, r = i + len - 1;
            bool ok = true;
            while (l < r) {
                if (s[l] != s[r]) { ok = false; break; }
                ++l; --r;
            }
            if (ok) return s.substr(i, len);
        }
    }
    return "";
}

int main() {
    vector<string> tests = {"babad", "cbbd", "abssbm", "dsadasjh", ""};
    for (auto &t : tests) {
        cout << "'" << t << "' -> '" << longestPalindromeBrute(t) << "'" << endl;
    }
    return 0;
}
```
**Compile & run:**
```bash
g++ -std=c++17 -O2 -o longest_brute longest_brute.cpp
./longest_brute
```

---

### Expand Around Center (optional, Python)
A frequently used alternative is **expand-around-center** which tries to expand palindromes from each center (each character and between-character center). It runs in `O(n^2)` time but uses `O(1)` extra space.

**Python implementation (concise):**
```python
def longest_palindrome_expand_center(s: str) -> str:
    if not s:
        return ""
    start = 0
    max_len = 1
    n = len(s)

    def expand(l, r):
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        # after loop, palindrome is s[l+1:r]
        return (l + 1, r - 1)

    for i in range(n):
        # odd-length
        l, r = expand(i, i)
        if r - l + 1 > max_len:
            start, max_len = l, r - l + 1
        # even-length
        l, r = expand(i, i + 1)
        if r - l + 1 > max_len:
            start, max_len = l, r - l + 1

    return s[start:start + max_len]
```

---

## Complexity Analysis

- **Brute-Force (C++)**
  - Time: `O(n^3)` — triple nested behavior (choose length, choose start, check palindrome).
  - Space: `O(1)` (ignoring input / output substrings).

- **Dynamic Programming (Python)**
  - Time: `O(n^2)` — filling the `n x n` table.
  - Space: `O(n^2)` — the DP table `dp`.

- **Expand-Around-Center (Python)**
  - Time: `O(n^2)` — expanding from each center.
  - Space: `O(1)` — only a few indices stored.

---

## Mathematical Note: Number of Substrings
For a string of length `n`, the number of non-empty substrings is:
\[
\sum_{k=1}^{n} k = rac{n(n+1)}{2}
\]
Explanation: for each start position `i` (1..n) there are `(n-i+1)` possible substrings; summing yields the formula above.

---

## Conclusion
Both dynamic programming and brute-force strategies solve the longest palindromic substring problem. The dynamic approach avoids repeated checks at the cost of `O(n^2)` memory. Brute force uses constant extra memory but runs slower for large `n`. The expand-around-center method offers a pragmatic balance: `O(n^2)` time with `O(1)` space and is often used in practical code.

This README was created by carefully converting the uploaded document `Longest Palindromic Substring.docx`. fileciteturn0file0

---

## Sources
- Problem inspiration / course document: *Longest Palindromic Substring* (Sina Rajabi & Raya Faezinia). fileciteturn0file0  
- LeetCode — Dynamic Programming problem lists.  
- Wolfram MathWorld — Sum of first n integers.
