#this program used for calculates factorial and this program developed by madhanraj_official
def madhan(o):
  if o==1 or o==0:
    return 1
      
  else:
    return o*madhan(o-1)            #1x2x3x4x5=120. like n x n(number of time -1)



n=int(input("enter tha value for factorial calculation :"))     #input for factorial numbers
if n<0:
  print("negative numbers doesn't exist in factorial")             # factorial part doesn't exist negative numbers
elif n==0 or n==1:
  print('the factorial value of',n,'is', madhan(n))             #the value of 0 or 1 is return factorial value is 1
else:
  print('the factorial value of',n,'is',madhan(n))            #factorial number greater than 1 value is executed by this line
  
  