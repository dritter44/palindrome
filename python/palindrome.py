def palindrome(word):
    input_word = ""
    if type(word) is int:
        input_word = str(word)
    else:
        input_word = word
    #print(type(input_word))
    cln_str = ''
    for letter in input_word:
        if letter.isalnum():
            cln_str = cln_str + letter
    cln_str1 = cln_str.lower()
    #return cln_str1
    if (len(cln_str1) == 2 or len(cln_str1) == 3) and (cln_str1[0] == cln_str1[len(cln_str1)-1]):
        return True
    if (len(cln_str1) >= 4) and (cln_str1[0] == cln_str1[len(cln_str1)-1]):
        return palindrome(cln_str1[1:len(cln_str1)-1])
    else:
        return False

    # Write code here
print(palindrome('A man, a plan, a canal -- Panama'))