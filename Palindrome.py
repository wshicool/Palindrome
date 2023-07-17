def Palindrome(s):
    return s == s [::-1]


s = "balls"
ans = Palindrome(s)


if ans:
    print("Yes")
else:    
    (print("No"))