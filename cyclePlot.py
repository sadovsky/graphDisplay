import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

''' plots giant component'''
def cyclePlot(gexFile):
    DG = nx.DiGraph(nx.read_gexf(gexFile))
    
    #generate networkx friendly position format
    #dictionary keyed by node label with values being a float32 ndarray
    pos = dict()
    for i in range(1, len(DG.node)+1):
        xPos = DG.node[str(i)]['viz']['position']['x']
        yPos = DG.node[str(i)]['viz']['position']['y']
        pos[str(i)] = np.array([xPos,yPos])
    
    #nx.draw_networkx_edges(DG,pos,nodelist=DG.node.keys(),alpha=0.05,
    #                       arrows=True)
    nx.draw_networkx_nodes(DG,pos,nodelist=DG.node.keys(),
                       node_size=30,
                       node_color='grey',
                       alpha=0.4)
    nx.draw_networkx_edges(DG,pos,alpha=0.4,
                               arrows=True,
                               edge_color='k')
    plt.show()
    
    scc=nx.strongly_connected_component_subgraphs(DG)
    CG=scc[0];
    
    #show example
    nx.draw_networkx_nodes(CG,pos,nodelist=CG.node.keys(),
                       node_size=30,
                       node_color='c')
    nx.draw_networkx_edges(CG,pos,alpha=0.5,
                               arrows=True,
                               edge_color='r')

cyclePlot("demo.gexf")
plt.figure();
cyclePlot("demoPerm.gexf")