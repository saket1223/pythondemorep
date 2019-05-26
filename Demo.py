def search(list,n):
  for i in len(list):
    if list[i]==list[n]:
      return True;
    else:
      return False;
      
     
     
list =[2,4,5,6,7,81,3]
n=5
if search(list,n):
  print('Found');
else:
  print('Not found')
