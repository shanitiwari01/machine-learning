def isPalindrome(str):
    if str and str == str[::-1]:
       return True
    return False

isPalindromeWord = isPalindrome('oyo')

print(isPalindromeWord)