# -*- coding: utf-8 -*-
"""Palindrome Check.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/112u_9C5LbaADMf7bfM5uNuc7aT3iZSNd
"""

#Following Code will check if given text string is Palendrome or not
def is_palindrome(text):
  import re
  Special_char = ",!.?'-"
  if len(text)<=1000:
    text1=re.sub("[,!.?'-]","",text)
    #print(text1)
    text1 = text1.lower()
    text1 = text1.replace(" ","")
    if text1 == text1[::-1]:
      print("YES")
    else:
      print("NO")

text = "Too hot to hoot."
is_palindrome(text)