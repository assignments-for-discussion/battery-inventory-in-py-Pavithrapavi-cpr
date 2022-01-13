def count_batteries_by_usage(cycles):
  
    lowCount= 0
    mediumCount= 0
    highCount= 0
  


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n")
count_batteries_by_usage = [100, 300, 500, 600, 900, 1000]
  
for i in count_batteries_by_usage:
  if i<400:
    lowcount=lowcount+1
  elif i==400 and i<=919:
    mediumcount=mediumcount+1
  else:
     highcount=highcount+1
print("done counting:")
