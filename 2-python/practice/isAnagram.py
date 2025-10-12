def isAnagram(str1, str2):
    if str1.lower() == str2[::-1].lower():
        return True
    return False

print(isAnagram("Shani", "Inahs"))