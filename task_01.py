def is_palindrome (s):
  s = s.casefold()
  out = ''
  
  for i in range(len(s)):
    n = ord(s[i])
    if (n >= 48 and n <= 57 or n >= 97 and n <= 122):
      out += (s[i])
  
  if (out == out[::-1]):
    return True
  else:
    return False
