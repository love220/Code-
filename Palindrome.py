# To find whether a word/string Entered is a Palindrome or not

word = str(input('Enter a Word: '))

rvs =word[::-1]
print(rvs)

if rvs == word:
  print('It is a Palindrome')
else:
  print('It is not a Palindrome')
  
