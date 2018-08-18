import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
	graph = nx.Graph()
	return graph

def join(graph,user):
	graph.add_node(user)

def connect(graph,user1,user2):
	graph.add_edge(user1,user2)

def no_of_users(graph):
	return len(practice_graph.nodes())

def draw_graph(graph):
	nx.draw(graph, with_labels=True)
	plt.savefig("graph-drawing.pdf")
    plt.show()

def friends(graph, user):
    return set(graph.neighbors(user))  

def friends_of_friends(graph, user):
	friends_list =  friends(graph,user)
	friends_of_friends_list = set()
	for friend in friends_list:
		current_fof_list = friends(graph,friend)
		for fof in current_fof_list:
			if fof == user:
				continue	
			friends_of_friends_list.add(fof)

	return friends_of_friends_list-friends_list

def mutual_friends(graph, user1, user2):
    friend1_list = friends(graph,user1)
    friend2_list = friends(graph,user2)	
    return friend1_list.intersection(friend2_list)


def number_of_common_friends_map(graph, user):
	fof_list = friends_of_friends(graph,user)
	dict_of_common_friends_count = {}
	for fofs in fof_list:
		dict_of_common_friends_count[fofs]=len(mutual_friends(graph,user,fofs))
	return dict_of_common_friends_count	

def number_map_to_sorted_list(map_of_common_friends):
    sorted_list = [v[0] for v in sorted(map_of_common_friends.iteritems(), key=lambda (k, v): (-v, k))]
	return sorted_list







