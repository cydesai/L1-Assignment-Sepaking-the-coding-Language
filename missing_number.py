# -*- coding: utf-8 -*-
"""Missing Number.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-51Pdl1o6OBHg71Hl-WC0wtBWRPKI3Zg
"""

# Follwing Code will return the missing numbers from the given list.
def find_missing_number(numbers):
  missing_number = []
  for i in range(1, 10):
    if i in numbers:
      continue
    else:
      missing_number.append(i)
  print(missing_number)


find_missing_number([1, 2, 3, 4, 6, 7, 10])