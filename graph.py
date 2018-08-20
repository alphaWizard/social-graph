import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict


def create_graph():
	graph = nx.Graph()
	return graph


def join(graph,user):
	graph.add_node(user)


def are_friends(graph,user1,user2):
	return graph.has_edge(user1,user2)

def connect(graph,user1,user2):
	if not graph.has_node(user1):
		join(graph,user1)
	if not graph.has_node(user2):
		join(graph,user2)	
	if not graph.has_edge(user1,user2):
		graph.add_edge(user1,user2)


def no_of_users(graph):
	return len(graph.nodes())


def draw_graph(graph):
	if len(graph.edges()) > 50:
		return
	nx.draw(graph , with_labels=True)
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


def network_triads(graph,user):
	triads_list = []
	flist = friends(graph,user)
	for f in flist:
		flist2=friends(graph,f)
		for cf in flist2:
			if cf ==user:
				continue
			if graph.has_edge(user,cf) and f<cf:
				triads_list.append((user,f,cf))
				if len(triads_list) == 20:
					return triads_list
	return triads_list				



def no_of_components(graph):
	return len(list(nx.connected_components(graph)))



def in_same_network(graph,user1,user2):
	if graph.has_node(user1) == False:
		return False
	if graph.has_node(user2) == False:
		return False	
	vis = defaultdict(lambda: False)
	queue = []
	queue.append(user1)
	vis[user1] = True
	while queue:
		s = queue.pop(0)
		if s == user2:
			return True
		flist = friends(graph,s)
		for ff in flist:
			if vis[ff] == False:
				queue.append(ff)
				vis[ff]=True

	return False



def number_of_common_friends_map(graph, user):
	fof_list = friends_of_friends(graph,user)
	dict_of_common_friends_count = {}
	for fofs in fof_list:
		dict_of_common_friends_count[fofs]=len(mutual_friends(graph,user,fofs))
	return dict_of_common_friends_count	



def number_map_to_sorted_list(map_of_common_friends):
	sorted_list = [v[0] for v in sorted(map_of_common_friends.iteritems(), key=lambda (k, v): (-v, k))]
	return sorted_list


def recommend_by_number_of_common_friends(graph, user):
    return number_map_to_sorted_list(number_of_common_friends_map(graph,user))



def influence_map(graph, user):
	flist = friends(graph,user)
	foflist = friends_of_friends(graph,user)
	influence_dict = {}
	for fof in foflist:
		influence_dict[fof]= float(0)
		for f in flist:
			if not graph.has_edge(f,fof):
				continue
			length = float(len(friends(graph,f)))
			influence_dict[fof] = influence_dict[fof]+ float(1/length)

	return influence_dict		



def recommend_by_influence(graph, user):
	return number_map_to_sorted_list(influence_map(graph,user))