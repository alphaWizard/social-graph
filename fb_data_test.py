from graph import *


network = create_graph()

with open('facebook-data.txt') as f:
	for i,line in enumerate(f):
		x = line.split()
		a,b = int(x[0]), int(x[1])
		connect(network,a,b)	
    		


print no_of_users(network)  

print recommend_by_number_of_common_friends(network,28000)[:10]

print recommend_by_influence(network,28000)[:10]

print network_triads(network,1)