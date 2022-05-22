import sys
for line in sys.stdin:
	line = line.strip()
	years, states, months, numbers, dates = line.split()
	
	#print('%s\t%s' %(years,1))
	print('%s\t%s' %(states,1))
	#print('%s\t%s' %(months,1))
	#print('%s\t%s' %(numbers,1))
	#print('%s\t%s' %(dates,1))