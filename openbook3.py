def access_lists():
	transit_list = []
	management_list = []
	global_list = []
	fout = open("running-config.cfg","r")
	for line in fout:
		if("transit_access_in" in line):
			transit_list.append(line)
		if("global_access" in line):
			global_list.append(line)
		if("fw-management_access_in" in line):
			management_list.append(line)
	print(transit_list)
	print(management_list)
	print(global_list)

access_lists()
