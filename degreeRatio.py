import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def plotDegreeRatio(gexFile):
    #setup our digraph from a gexf (gephi) format #read_gexf
    DG = nx.DiGraph(nx.read_gexf(gexFile))
    
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
    #node labels start at 1
    for i in range(1,len(DG.node)+1):   
        #dont want to divide by zero, we'll handle this below
        if outDeg[str(i)] != 0:
            #degrees are ints so convert
            degreeRatio[str(i)] = float(inDeg[str(i)]) / float(outDeg[str(i)])
            #we're going to drop it to 1 when over 1    
            if degreeRatio[str(i)]>1:
                degreeRatio[str(i)]=1
        #in this case, we'll set +inf to 1
        elif inDeg[str(i)] > 0:
            degreeRatio[str(i)]=1
        else: #both were zero
            degreeRatio[str(i)]=0
        
    #draw!
    nx.draw_networkx_edges(DG,pos,nodelist=degreeRatio.keys(),alpha=0.05,
                           arrows=True)
    nx.draw_networkx_nodes(DG,pos,nodelist=degreeRatio.keys(),
                       node_size=20,
                       node_color= degreeRatio.values(),
                       cmap=plt.cm.jet)
    plt.show()
    
plt.figure(figsize=(6*3.13,4*3.13))
plt.subplot(1,2,1, aspect='equal')
plt.title('Data In/Out Degree Ratio')
plt.axis('off');
plotDegreeRatio(r"demo.gexf")

plt.subplot(1,2,2, aspect='equal')
plt.title('Randomized Graph In/Out Degree Ratio')
plt.axis('off');
plotDegreeRatio(r"demoRand.gexf")

plt.savefig('results.pdf')
