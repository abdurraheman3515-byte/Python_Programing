for num in range(1,1000000):
   totel= 0 


   for i in range(1,num):
      if num % i == 0 :
         totel += i

   if totel == num:
      print(num)    