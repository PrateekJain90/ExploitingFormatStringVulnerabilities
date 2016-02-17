with open('procMap.txt') as f:
	zones = []
	contents = f.read();
	for line in contents.split('\n'):
		if not line:
			continue
		memrange, perms, _ = line.split(None, 2)
		start, end = memrange.split('-')
		zones.append({
			'start': int(start, 16),
			'end': int(end, 16),
			'perms': perms
		})

with open('address.txt') as f:
	address = f.read().splitlines()				

for index in range(len(address)):
	for mapping in zones:
		if mapping["start"] <= int(address[index],16) < mapping["end"]:
			break

	# Check the memory permissions
	if "w" in mapping["perms"]:
		print("Format function no. %d has format string in writable memory." % (index+1));


