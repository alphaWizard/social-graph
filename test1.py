from graph import *

network = create_graph()
join(network,"a")
join(network,"b")
join(network,"c")
join(network,"d")
join(network,"e")
join(network,"f")
connect(network,"a","b")
connect(network,"a","d")
connect(network,"d","b")
connect(network,"b","c")
connect(network,"c","e")
connect(network,"e","d")

print recommend_by_number_of_common_friends(network,"e")


