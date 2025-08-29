#include <iostream>
using namespace std;

bool isPalindrome(const string& s, int start, int end) {
    while (start < end)
    {
        if (s[start] != s[end]) return false;
        start++;
        end--;
    }
    return true;
}
string longestPalindrome(string s)
{
    int n = s.length();
    for (int len = n; len >= 1; len--)
    {
        for (int start = 0; start + len - 1 < n; start++)
        {
            int end = start + len - 1;
            if (isPalindrome(s, start, end))
            {
                return s.substr(start, len);
            }
        }
    }
    return "";
}
int main()
{
    string input;
    cin >> input;
    cout << longestPalindrome(input) << endl;
}