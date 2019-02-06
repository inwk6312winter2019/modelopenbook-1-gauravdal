
def list_ifname_ip():
	config_key = {}
	key = []
	ip_addr = []
	fout = open("running-config.cfg" ,"r")
	for line in fout:
		if("nameif" in line):
			temp_key = line.split()
			if("nameif"!= temp_key[1]):
				print(temp_key[1])
		if("ip address" in line):
			temp_ip = line.split()
			if("ip"== temp_ip[0]):
				print(temp_ip[2:])
	config_key

list_ifname_ip()
