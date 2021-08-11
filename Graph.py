class Graph:
    graph={}
    def __init__(self):
        pass

    def addEdge(self, u, v, w):# ADD EDGES TO THE GRAPH
        if u not in self.graph:
            self.graph[u]=[[v,w]]
        else:
            self.graph[u].append([v,w])
        self.completeGraph()

    def completeGraph(self): # CREATE A FULL GRAPH FOR EVERY VERTEX EVEN FOR THOSE VERTEX WHO IS NOT DIRECTED TO ANY OTHER NEIGHBOR
        t = self.getDistinctVertexinternal()
        for x in t:
            if x not in self.graph:
                self.graph[x]=[]

    def getDistinctVertexinternal(self):
        t=[x for x in self.graph.keys()]
        for x in self.graph.values():
            for y in x:
                if y[0] not in t:
                    t.append(y[0])
        return t

    def getGraph(self):# RETURN GRAPH
        return self.graph

    def printGraph(self): # PRINT GRAPH
        print(self.graph)

    def getDistinctVertex(self):# RETURN ALL THE VERTICES
        return [x for x in self.graph.keys()]

    def getVertexCount(self):# RETURN NUMBER OF VERTICES
        return len(self.getDistinctVertex())

    def getEmptyGraphDic(self): # RETURN EMPTY DICTIONARY WITH ALL THE VERTICES AS KEY WITH INF AS THEIR VALUE
        t={}
        for x in self.getDistinctVertex():
            t[x]=float("Inf")
        return t
