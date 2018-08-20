from graph import *

network = create_graph()
connect(network,"Nurse","Juliet")

connect(network,"Juliet","Tybalt")
connect(network,"Juliet","Capulet")
connect(network,"Juliet","Friar Laurence")
connect(network,"Juliet","Romeo")

connect(network,"Capulet","Tybalt")
connect(network,"Capulet","Escalus")
connect(network,"Capulet","Paris")

connect(network,"Friar Laurence","Romeo")

connect(network,"Romeo","Benvolio")
connect(network,"Romeo","Montague")
connect(network,"Romeo","Mercutio")

connect(network,"Benvolio","Montague")

connect(network,"Montague","Escalus")

connect(network,"Escalus","Paris")
connect(network,"Escalus","Mercutio")

connect(network,"Paris","Mercutio")



#Testing with assertions 
assert len(network.nodes()) == 11
assert len(network.edges()) == 17

assert mutual_friends(network, "Mercutio", "Nurse") == set()
assert mutual_friends(network, "Mercutio", "Romeo") == set()
assert mutual_friends(network, "Mercutio", "Juliet") == set(["Romeo"])
assert mutual_friends(network, "Mercutio", "Capulet") == set(["Escalus", "Paris"])
assert number_of_common_friends_map(network, "Mercutio") == { 'Benvolio': 1, 'Capulet': 2, 'Friar Laurence': 1, 'Juliet': 1, 'Montague': 2 }
assert recommend_by_number_of_common_friends(network, "Mercutio") == ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']
print influence_map(network, "Mercutio") == { 'Benvolio': 0.2, 'Capulet': 0.5833333333333333, 'Friar Laurence': 0.2, 'Juliet': 0.2, 'Montague': 0.45 }
assert recommend_by_influence(network, "Mercutio") == ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


