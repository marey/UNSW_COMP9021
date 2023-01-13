Say that two strings s1 and s2 can be merged into a third string s3 if s3 is obtained from s1 by inserting arbitrarily in s1 the characters in s2, respecting their order. For instance, the two strings ab and cd can be merged into abcd, or cabd, or cdab, or acbd, or acdb, ..., but not into adbc nor into cbda. Write a program merging_strings.py that prompts the user for 3 strings and displays the output as follows:

If no string can be obtained from the other two by merging, then the program outputs that there is no solution.

Otherwise, the program outputs which of the strings can be obtained from the other two by merging.

Here are possible interactions:

Please input the first string: ab
Please input the second string: cd
Please input the third string: abcd
The third string can be obtained by merging the other two.
Please input the first string: ab
Please input the second string: cdab
Please input the third string: cd
The second string can be obtained by merging the other two.
Please input the first string: abcd
Please input the second string: cd
Please input the third string: ab
The first string can be obtained by merging the other two.
Please input the first string: ab
Please input the second string: cd
Please input the third string: adcb
No string can be merged from the other two.
Please input the first string: aaaaa
Please input the second string: a
Please input the third string: aaaa
The first string can be obtained by merging the other two.
Please input the first string: aaab
Please input the second string: abcab
Please input the third string: aaabcaabb
The third string can be obtained by merging the other two.
Please input the first string: ??got
Please input the second string: ?it?go#t##
Please input the third string: it###
The second string can be obtained by merging the other two.
Insert your code into merging_strings.py.

If you are stuck, but only when you are stuck, then use merging_strings_scaffold.py.