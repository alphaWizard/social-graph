from graph import *

network = create_graph()
join(network,"g")
connect(network,"a","b")
connect(network,"a","c")
connect(network,"b","c")
connect(network,"b","d")
connect(network,"c","d")
connect(network,"c","f")
connect(network,"d","e")
connect(network,"d","f")

draw_graph(network)

print are_friends(network,"c","a")
print network_triads(network,"c")
print recommend_by_number_of_common_friends(network,"a")

print recommend_by_influence(network,"a")
		
print in_same_network(network,"g","b")