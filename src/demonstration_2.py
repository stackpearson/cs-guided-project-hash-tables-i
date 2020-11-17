"""
You've uncovered a secret alien language. To your surpise, the language is made
up of all English lowercase letters. However, the alphabet is possibly in a
different order (but is some permutation of English lowercase letters).
​
You need to write a function that, given a sequence of words written in this
secret language, and the order the alphabet, will determine if the given words
are sorted "alphabetically" in this secret language.
​
The function will return a boolean value, true if the given words are sorted
"alphabetically" (based on the supplied alphabet), and false if they are not
sorted "alphabetically".
​
Example 1:
​
```plaintext
Input: words = ["lambda","school"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'l' comes before 's' in this language, then the sequence is
sorted.
```
​
Example 2:
​
```plaintext
Input: words = ["were","where","yellow"], order = "habcdefgijklmnopqrstuvwxyz"
Output: false
Explanation: As 'e' comes after 'h' in this language, then words[0] > words[1],
hence the sequence is unsorted.
```
​
Example 3:
​
```plaintext
Input: words = ["lambda","lamb"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first four characters "lamb" match, and the second string is
shorter (in size.) According to lexicographical rules "lambda" > "lamb",
because 'd' > '∅', where '∅' is defined as the blank character which is less
than any other character (https://en.wikipedia.org/wiki/Lexicographic_order).
```
​
Notes:
​
- order.length == 26
- All characters in words[i] and order are English lowercase letters.
"""
def are_words_sorted(words, alpha_order):
    """
    Inputs:
    words: List[str]
    alpha_order: str
​
    Output:
    bool
    """
    # Your code here
    # if we didn't have to consider an alternate ordering, 
    # we could just iterate through our words two-at-a-time and 
    # check that every pair of words are in sorted order 
    
    # how do we change our logic to check for a different alphabetical ordering? 
    # for each letter in the alphabet, we need to be able to know what comes after 
    # this letter in the altered alphabetical ordering 
    # one way we could do this is to store each letter with its index in the 
    # altered ordering
    # we'll init a dict to keep track of letters as keys and their altered indices 
    # as values 
    altered_order = {letter: index for index, letter in enumerate(alpha_order)} 
    # that way, we can look up each letter in our dict to figure out its altered index
    # once we have the altered indices we can check that they're in the right order 
    
    for i in range(1, len(words)):
        word1 = words[i-1]
        word2 = words[i]
        # iterate through each of the characters of the two words 
        # and check that the current letters adhere to the altered ordering 
        for j in range(min(len(word1), len(word2))):
            char1 = word1[j]
            char2 = word2[j]
            print(altered_order[char1], altered_order[char2])
            # check each letter in both words
            if char1 != char2:
                if altered_order[char1] > altered_order[char2]:
                    return False
                else:
                    break
        
        # if we get out of this loop, and len(word1) > len(word2)
        # return False 
        if len(word1) > len(word2):
            return False
​
    return True 
​
​
# print(are_words_sorted(["were","where","yellow"], "habcdefgijklmnopqrstuvwxyz"))
print(are_words_sorted(["lambda","school"], "hlabcdefgijkmnopqrstuvwxyz"))