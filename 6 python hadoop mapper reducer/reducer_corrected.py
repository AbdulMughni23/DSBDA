import sys
	

prev_value = None
prev_count = 0

for line in sys.stdin:
	line = line.strip()
	value, count = line.split('\t')

	count=int(count)
	prev_count += count

	
	if prev_value == value:
		prev_count += count
	else:
		if prev_value:
			print('%s\t%s' % (prev_value, prev_count))
		prev_count = count
		prev_value = value
if prev_value == value:
	print('%s\t%s' % (prev_value, prev_count))
