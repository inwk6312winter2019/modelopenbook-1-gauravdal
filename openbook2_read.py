def replace_ip():
	fout = open("running-config.cfg","r")
	fin = open("replaced_running_config.txt","a")
	for line in fout:
		if("address" in line and "." in line):
			line = line.split()
			temp_ip = line[2].split(".")
			temp_mask = line[3].split(".")
			if(temp_ip[0] == "192"):
				
				temp_ip[0] = "10"
				temp_mask[0] = "255"
				temp_mask[1] = "0"
				temp_mask[2] = "0"
				temp_mask[3] = "0"
			if(temp_ip[0] == "172"):
				temp_ip[0] = "10"
				temp_mask[0] = "255"
				temp_mask[1] = "0"
				temp_mask[2] = "0"
				temp_mask[3] = "0"

			line = line[0]+line[1] +" "+ ".".join(temp_ip)+" "+".".join(temp_mask)
			fin.write(line)
		else:
			fin.write(line)

replace_ip()


