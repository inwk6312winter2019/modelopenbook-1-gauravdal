
def list_ifname_ip():
	config_key = {}
	fout = open("running-config.cfg" ,"r")
	for line in fout:
		if("nameif" in line):
			temp_key = line.split()
			if("nameif"!= temp_key[1]):
				print(temp_key[1])
	fout.seek(0)
	for line in fout:
		if("ip address" in line):
			temp_ip = line.split()
			print(temp_ip)

list_ifname_ip()
