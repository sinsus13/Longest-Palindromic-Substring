class Brute_Force:

    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


    def longest_palindrome(self, s : str) -> str:
        n = len(s)
        for length in range(n, 0, -1):  # decreasing substring length
            for start in range(n - length + 1):
                end = start + length - 1
                if self.is_palindrome(s, start, end):
                    return s[start:start + length]
        return ""


if __name__ == "__main__":
    input_str = input()
    print(Brute_Force().longest_palindrome(input_str))
