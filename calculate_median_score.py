# Following Code will calculate the Median Score of a given List
def calculate_median(scores):
  import math
  scores.sort()
  list_len = len(scores)
  if list_len%2==0:
    a=list_len/2
    d=int(a-1)
    avg=(scores[d]+scores[d+1])/2
    print(avg)
    #print(avg)
  else:
    b=list_len/2
    c=math.floor(b)
    print(scores[c])

scores = [85, 90, 78, 82, 95, 88]
calculate_median(scores)
