def high_scores (numbers):
  return list(filter(lambda x:x%2==0, numbers))
  
print(high_scores([0,1,2,3,4,5,6,7,8,9,10]))
