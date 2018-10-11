import networkx as nx
import os 


'''
change 'C:\\Users\\Ines\\Desktop\\porgat.txt'
to the directory of your file

you can download the file by going to
http://bioinfo.uib.es/~joemiro/marvel/porgat.txt
right click the page and save it as a textfile
'''

def create_marvel_graph(file_name):
	G=nx.Graph() # marvel graph
	mar = open(os.path.join(os.getcwd(), file_name), 'rb')
	for i, line in enumerate(mar.readlines()):
		if i>0 and i<19429:
			boo=False
			lab=''
			for ch in line.rstrip():
				if not boo:
					if ch==' ':
						boo=True				
				else:
					lab+=ch
			G.add_node(i,label=lab)

		elif i>19429: #line 19429 indicates that the following lines will have the edges
			m=line.rstrip().split()
			k=m.pop(0)
			while len(m)>0:
				l=m.pop(0)
				G.add_edge(int(k),int(l))
	return G
			
if __name__ == '__main__':
	G = create_marvel_graph('porgat.txt')

	print("number of nodes: "+str(G.number_of_nodes()))
	print("number of edges: "+str(G.number_of_edges()))

