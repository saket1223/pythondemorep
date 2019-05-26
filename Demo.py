pos = -1
def search(list,n):
  i = 0
  while i < len(list):
    if list[i]== n :
      globals()['pos'] = i
      return True
    i+=1
  return False
      
     
     
list =[2,4,5,6,7,81,3]
n=2
if search(list,n):
  print('Found at position ',pos+1 )
else:
  print('Not found')
