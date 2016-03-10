from random import randrange

table=[[0]*10 for x in xrange(20)]

finished = False

count = 0
while not finished:

 y = randrange(0,8) #Tuxaia thesi

 table[0][y] = 1
 table[1][y] = 1      #lamda
 table[2][y] = 1
 table[2][y+1] = 1




 for i in range(0,17):  #Check for free space
	 
  if table[i+3][y] == 0 and table[i+3][y+1] == 0:
   table[i+1][y] = 1
   table[i+2][y] = 1
   table[i+3][y] = 1
   table[i+3][y+1] = 1
   table[i][y] = 0
   table[i+2][y+1] = 0
   
  elif(table[0][y] == 1 or table[0][y+1] == 1):
   finished = True
   
  else:
   break
 count = count + 1
 for k in range(0,20):
  for j in range(0,10):
   print table[k][j],
  print "\n"
 c = raw_input("continue?")


print "The game is over," ,count ,"L managed to get in the game-table!"
print "Thank you for playing!"
