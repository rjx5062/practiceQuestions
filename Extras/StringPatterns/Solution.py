"""
Given the length of a word (wordLen) and the maximum number of consecutive vowels that it can contain (maxVowels.
Determine how many unique words can be generated. Words will consist of English alphabetic letters a through z 
only. Vowels are v. {a, e, i, o, u}; consonants are c. the remaining 21 letters. In the explanations, v and 
represent vowels and consonants.
Complete the function calculate Ways in the editor below.

calculateWays has the following parameter(s):
int wordLen: the length of a word 
int maxVowels: the maximum number of consecutive vowels allowed in a word

Returns: int: the number of well-formed strings that can be created, modulo 1000000007 (10°+7)

"""
"""
wordLen = 1
maxVowels = 1
Patterns: {V, C}
That means there are 26 possibilities, one for each letter in the alphabet.

wordLen = 4
maxVowels = 1
Patterns: {CCCC, VCCC, CVCC, CCVC, CCCV, VEVC, CVCV, VCCV}
There are 412,776 possibilities

wordLen = 4
maxVowels = 2
In this case, all of the combinations from the previous example are still valid.
• There are 5 additional patterns to consider, three with 2 vowels (wvcc, cc, cc) and 2 with 3 vowels 
(vvcv and vcv).
• Their counts are 3 * (5 * 5 * 21 * 21) = 3 * 11025 = 33075 + 2 * (5 * 5 * 5 * 21) = 2 * 2625 = 5250.
• The total number of combinations then is 412776 + 33075 + 5250 = 451101.

The result may be a very large number, so return the answer modulo (10°+7).

"""




from typing import *
class Solution():

    # dynamo = [1000][1000]

    def stringPattern(self, wordLen: int, maxVowels: int, remVowels: int) -> int:

        withVowel, withoutVowel = 0, 0

        if wordLen == 0:
            return 1

        if dynamo[wordLen][remVowels] != -1:
            return dynamo[wordLen][remVowels]

        if remVowels > 0:
            withVowel = (5 *
                         self.stringPattern(wordLen - 1, maxVowels, remVowels - 1)) % 1000000007
            withoutVowel = (21 *
                            self.stringPattern(wordLen - 1, maxVowels, maxVowels)) % 1000000007
        else:
            withoutVowel = (21 *
                            self.stringPattern(wordLen - 1, maxVowels, maxVowels)) % 1000000007

        dynamo[wordLen][remVowels] = withoutVowel + withVowel

        # print(dynamo[wordLen][remVowels])
        return withoutVowel + withVowel

    def calculateWays(self, wordLen: int, maxVowels: int) -> int:

        global dynamo
        dynamo = [[-1 for _ in range(maxVowels + 1)]
                  for _ in range(wordLen + 1)]

        ans = int(self.stringPattern(
            wordLen, maxVowels, maxVowels) % 1000000007)
        print(ans)
        return ans


if __name__ == "__main__":
    s1 = Solution()
    s1.calculateWays(4, 2)
