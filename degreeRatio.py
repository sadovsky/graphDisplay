import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#TODO functionalize this so we can compare multiple datasets

#setup our digraph from a gexf (gephi) format #read_gexf
DG = nx.DiGraph(nx.read_gexf("C:\Users\sadovsky\Documents\GitHub\graphDisplay\demoRand.gexf"))

#turn node labels into dictionary node keys
DG = nx.relabel_gexf_graph(DG)

#generate networkx friendly position format
#dictionary keyed by node label with values being a float32 ndarray
pos = dict()
for i in range(1, len(DG.node)+1):
    xPos = DG.node[str(i)]['viz']['position']['x']
    yPos = DG.node[str(i)]['viz']['position']['y']
    pos[str(i)] = np.array([xPos,yPos])

#get degree ratio (in to out) for color information
inDeg = DG.in_degree()
outDeg = DG.out_degree()

degreeRatio = dict()
for i in range(1,len(DG.node)+1):
    #we will not consider zero outdegree cases
    if outDeg[str(i)] != 0:
        degreeRatio[str(i)] = inDeg[str(i)] / outDeg[str(i)]
    #else:
        #TODO should this be zero?  or should we catch it and make them grey?
        #degreeRatio[str(i)] = 0;
        
#TODO should normalize the ratio here so its the same between files
    
#draw!
#TODO: using the keys as the nodelist is a hack, we should use all and grayout
nx.draw_networkx_edges(DG,pos,nodelist=degreeRatio.keys(),alpha=0.1)
nx.draw_networkx_nodes(DG,pos,nodelist=degreeRatio.keys(),
                   node_size=80,
                   node_color=degreeRatio.values(),
                   cmap=plt.cm.jet)
plt.show()