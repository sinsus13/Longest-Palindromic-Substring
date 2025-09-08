5/2/2025








![](Aspose.Words.41a29872-f979-4be2-928f-56b471e335e5.001.png)![](Aspose.Words.41a29872-f979-4be2-928f-56b471e335e5.002.png)![](Aspose.Words.41a29872-f979-4be2-928f-56b471e335e5.003.png)


#
# <a name="_toc198459524"></a>Table of Contents

[Table of Contents	2](#_toc198459524)

[Problem	3](#_toc198459525)

[Solutions	3](#_toc198459526)

[Dynamic Programming Solution	4](#_toc198459527)

[Brute-Force Solution	6](#_toc198459528)

[Comparing Different Solutions	8](#_toc198459529)

[Complexity analysis	8](#_toc198459530)

[Time Complexity	8](#_toc198459531)

[C++ Brute-Force Approach:	8](#_toc198459532)

[Python Dynamic Programming Approach:	8](#_toc198459533)

[Space Complexity	9](#_toc198459534)

[C++ Brute-Force Approach:	9](#_toc198459535)

[Python Dynamic Programming Approach:	9](#_toc198459536)

[Mathematical Calculations	9](#_toc198459537)

[Conclusion	10](#_toc198459538)

[Sources	10](#_toc198459539)







Longest Palindromic Substring 

By: Raya Faezinia and Sina Rajabi

# <a name="_toc198459525"></a>Problem XE "Problem" 
To understand the problem, we must first know what a palindrome is. A palindrome, by definition, is a word, phrase, or sequence that reads the same backwards as forwards. For example, the word “racecar” is written the same both forwards and backwards making it a palindrome. Now, knowing the definition of a palindrome, we move on to the actual problem. The problem states given a string of text, find the longest palindrome substring within the main string. For example: the string “dsadasjh” in which the longest palindromic expression is “sadas”.

# <a name="_toc198459526"></a>Solutions XE "Solutions" 
To solve the problem given above, we have used two methods, within this article we will analyze both methods and compare their advantages and disadvantages. The first solution uses dynamic programming and memorization of substrings to help speed up the process of finding the largest substrings, while the second solution is a more brute-force approach. We will analyze both approaches in more detail later on. 

The base idea in both approaches is the same, where a square matrix, with the length and width of the given string is used to process and store all substrings. The substrings are determined by the ‘i’ and ‘j’ variables which control the start and end point of said substrings, where ‘i’ is the index of the starting character of the substring and ‘j+1’ is the index of the ending character.




# <a name="_toc198459527"></a>Dynamic Programming Solution XE "Dynamic Programming Solution" 
The algorithm for the dynamic programming solution involves filling a matrix diagonally starting from the main diagonal and making our way up.

The function for the algorithm is as follows:

Fij= True        Si=Sj+1 &&&&&&&&&, &&&&&&&&& Fi+1 j-1=True  False      Si≠Sj+1  

As explained above and to gain a better understand the solutions, we will use the string “abssbm” as an example. First a square matrix with a length and width of | abssbm | = 6 is generated.

000102030405101112131415202122232425303132333435404142434445505152535455

Assuming the indexing of the matrix matches the indexing of substrings, the entire bottom triangle of the matrix is the same as the top, just in an inverse order, making the matrix an upper triangular matrix. To add on, singular letters are always considered palindromes therefore the main diagonal of the matrix is considered True.

T0102030405FT12131415FFT232425FFFT3435FFFFT45FFFFFT



Now beginning from the diagonal above the main diagonal (substring with the length of 2) we analyze whether or not the substring is a palindrome or not and record it in the matrix.

TF02030405FTF131415FFTT2425FFFTF35FFFFTFFFFFFT

And similarly, the 3<sup>rd</sup> diagonal is also filled.

TFF030405FTFF1415FFTTF25FFFTFFFFFFTFFFFFFT

And now, for the 4<sup>th</sup> diagonal, we may utilize memorization and the matrix we have been filling to help speed up the process of analyzing whether the substring is a palindrome.

For instance, only the first and last letters of the index a14 are checked to see whether they're the same. We could proceed without examining the <a name="_hlk197541385"></a>internal slice between the first and the last letters. Assuming the internal slice is valid, the substring is a palindrome. Using the table with this strategy, we can fill the entire upper triangle of the matrix.

TFFFFFFTFFTFFFTTFFFFFTFFFFFFTFFFFFFT

Whilst filling the matrix up, we can keep a record of the indexes (i & j) of the last palindromic substring marked true in the matrix. Once the matrix is complete, the largest palindromic substring will have been found.

![](Aspose.Words.41a29872-f979-4be2-928f-56b471e335e5.004.png)An example of a program (in python) required to complete the mentioned operations is demonstrated below:


# <a name="_toc198459528"></a>Brute-Force Solution[^1] XE "Brute Force Solution" 
The second solution, which takes a more brute-force approach has the same conceptual idea as the dynamic programming solution. However, the matrix is not actually generated, and no data is saved. In this approach, starting from the top and going down, we analyze all substrings and stop when we find a match. For a clearer grasp of this method, the matrix below will be used to demonstrate the full process.

000102030405101112131415202122232425303132333435404142434445505152535455

In this approach we analyze every substring starting from the top right corner of the matrix (largest substring), and moving down and left from there, reducing the size of the string every time. As the problem only requires the largest substring palindrome, once a match is found the program stops and returns the final result.

In our example above, once the largest substring (“abssbm”) is analyzed and declared as non-palindromic. Therefor program moves to the second layer (“abssb” and “bssbm”). Essentially, the matrix is viewed as a pyramid and working from the top down we keep analyzing substrings until a match is found.

000102~~FFF~~10111213T~~F~~202122232425303132333435404142434445505152535455

An example of a program (in C++) required to complete the mentioned operations is demonstrated below:

![](Aspose.Words.41a29872-f979-4be2-928f-56b471e335e5.005.png)
# <a name="_toc198459529"></a>Comparing Different Solutions XE "Comparing Different Solutions" 
As seen above, the dynamic programming solution refrains from analyzing the same substring multiple times, in contrast to the brute-force method. However, unlike the dynamic programming method, the brute-force method does not generate and store information in a matrix. 

In terms of run time efficiency, the dynamic programming method avoids processing the precalculated substrings repeatedly. At the same time, due to the data stored in the generated matrix more memory would be occupied. 

The brute-force method will have a longer run time as it keeps analyzing substrings which have already been analyzed. On the other hand, as the matrix is not generated, it will have a smaller impact on the memory.

Depending on the application, both approaches have their pros and cons. If memory is limited, the brute-force approach is considered superior. If speed is more significant, the dynamic programming approach is a more reliable option.

# <a name="_toc198459530"></a>Complexity analysis
## <a name="_toc198459531"></a>Time Complexity
### <a name="_toc198459532"></a>C++ Brute-Force Approach:
This method utilizes three nested loops: an outer loop (indicating substring’s lengths), an inner loop (indicating starting index), and a palindrome check (used for character comparisons). Each of the named loops runs in O(n) time, resulting in a time complexity of O(n<sup>3</sup>).
> *O(n)×O(n)×O(n)=O(n<sup>3</sup>)*
### <a name="_toc198459533"></a>Python Dynamic Programming Approach:
In comparison to the Brute-Force Approach, this method has lower complexity, due to fewer loops. Only two loops --an inner loop and an outer loop-- are utilized, in contrast to the alternative method. Making the overall time complexity O(n<sup>2</sup>).
> *O(n)×O(n)=O(n<sup>2</sup>)*
## <a name="_toc198459534"></a>Space Complexity
### <a name="_toc198459535"></a>C++ Brute-Force Approach:
Compared to the dynamic approach, the brute-Force method uses only a few integers along with the input string. Ignoring auxiliary data structures (excluding the input), the space complexity is *O(1)*.
### <a name="_toc198459536"></a>Python Dynamic Programming Approach:
A 2-dimensional Boolean table *dp [ i] [ j]* is required to store whether the substring    *s [ i: j+1]* meets the palindromic condition. The table, sized n x n, is filled based on smaller subproblems as well as character matches. The space complexity is expected to be O(n<sup>2</sup>), as both the outer loop *(i*)* and the inner loop *(j)*, which construct the *dp* table iterate O(n) times. Overall, the table requires O(n<sup>2</sup>) space.

In brief, the time complexity of the brute-force is higher than that of dynamic programming. On the other hand, its space complexity is lower since all possibilities are calculated once but not recorded. Despite its memory efficiency, the dynamic programming approach is generally favored for larger values of n due to its faster runtime.

# <a name="_toc198459537"></a>Mathematical Calculations XE "Complexity analysis" 
To calculate the mathematical formula for the total number of non-empty substrings within a given string, we first assume a fixed starting position for the main string to derive substrings from. The variable ‘i’ is used to keep track of all the starting positions.

Assuming the starting position ‘i’, we can go all the way to ‘n’, as a result:

i=n-i+1





Sum of the overall starting positions is as follows:

i=1n(n-i+1)

=i=1nn+1- i=1ni

=n+1-n(n+1)2

=n(n+1)2

Solving the expression above, the total number of substrings within any given string of length ‘n’ is equal to:

n(n+1)2

# <a name="_toc198459538"></a>Conclusion XE "Conclusion" 
To sum up everything stated in this article, even though dynamic programming is a really powerful and versatile approach, it does come with its downsides. Depending on the circumstances, we can deduce the most appropriate approach, with all the considered restrictions, resulting in a preferable outcome. It is our job as software engineers and developers to examine the setting and choose the right path to follow.
# <a name="_toc198459539"></a>Sources
<https://leetcode.com/problem-list/dynamic-programming/>

<https://mathworld.wolfram.com/SumofFirstnIntegers.html> 

![A black and white sign with black text

AI-generated content may be incorrect.](Aspose.Words.41a29872-f979-4be2-928f-56b471e335e5.006.png)May 2nd, 2025\
Algorithm Design 
10


[^1]: Keep in mind this method is not truly a brute-force approach but due to its similarities and for the sake of simplicity, we will refer to it as such.