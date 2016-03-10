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


	

	for i in range(3,20):  #Check for free space
		if table[i][y] == 0 and table[i][y+1] == 0:
			tmp1 = table[i-1][y]
			table[i-1][y] = 0
			table[i][y] = tmp1
			tmp2 = table[i-1][y+1]
			table[i-1][y+1] = 0
			table[i][y+1] = tmp2
			tmp3 = table[i-2][y]
			table[i-2][y] = 0
			table[i-1][y] = tmp3
			tmp4 = table[i-3][y]
			table[i-3][y] = 0
			table[i-2][y] = tmp4
	
		elif table[4][y]== 1 and table[4][y+1] == 1 :
			finished = True
			
	count = count + 1
			

	  
print "The game is over," ,count ,"L managed to get in the game-table!"
print "Thank you for playing!" 
	
