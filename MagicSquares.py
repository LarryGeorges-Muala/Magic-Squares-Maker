#App Name: Magic Square Maker - Python
#Python Version 3.5
#Developper: Larry Georges Muala


#odd number input checking function
def oddCheck(n):
	n = int( input("\nPlease Enter an odd number: ") )
	
	if n % 2 != 0:
		magicSquare(n)
	else:
		oddCheck(n)

		
#magic square drawing function		
def magicSquare(n):	
	#creating the magic square layout and populating it with zeros
	magic_list = [[ 0 for column_s in range(n) ] for row_s in range(n)]


	#loops to assign magic square values to each entry in magic_list
	#using formula:
	# for Ith row and Jth column
	# value = { n*[(I + J - 1 + (n//2)) % n)] } + { [(I + 2*J - 2) % n] + 1 }

	for row_s in range(n):
		for column_s in range(n):
		
			row_value = row_s + 1
			column_value = column_s + 1

			value = ( n * ((row_value + column_value - 1 + (n//2)) % n) ) + ( ((row_value + 2 * column_value - 2) % n) + 1 )
			
			magic_list[row_s][column_s] = value
			
	print("")
	#formatting magic_list by splitting elements and joining by 4 digits space
	for m in range(n):
		print(' '.join( '{:4d}'.format(x) for x in magic_list[m] ))

		
		
#ask user for size of magic square, making sure it is a number
n = int( input("\nEnter the size of the magic square: ") )

#check that the input is odd with the oddCheck function
if n % 2 != 0:
	magicSquare(n)
	
else:
	oddCheck(n)