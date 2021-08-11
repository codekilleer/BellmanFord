import Graph  # importing User Defined Graph obejct to create and store graph


# BellmanFord Function
def BellmanFord(gr, graph, source):
    dist = gr.getEmptyGraphDic()  # CREATING EMPTY DICTIONARY TO STORE DISTANCE
    dist[source] = 0  # DEFINING 0 TO SOURCE NODE

    rep = False  # VARIABLE TO TRACK IF THE SOLUTION IS ACHIEVED WITHIN N-1 ITERATION STEP OR NOT IF YES THEN BREAK THE MAIN LOOP TO STOP WASTE TIME ON EXTRA UNECESSARY ITERATION.
    cycl = False  # BOOLEAN VARIABLE TO TRACK FOR LOOP IN THE GRAPH

    for _ in range(gr.getVertexCount()):  # OUTER LOOP RUNNING TILL N-1 TIMES

        if rep:  # CHECK ID ANY CHANGES HAPPENED IN PREVIOUS STEP OR NOT IF YES THEN BREAK THE LOOP TO PREVENT WASTE TIME ON EXTRA UNECESSARY ITERATION
            print("Iteration was done within N-1 Limit, that is in : ", _, " step(s)")
            break

        print("For Iteration ", _)  # PRINT THE TABLE FOR CURRENT ITERATION
        print("{0}\t\t{1}".format("Destination", "No of Hops"))
        for i in dist.keys():
            print("{0}\t\t\t\t{1}".format(i, dist[i]))

        rep = True

        for u in graph.keys():# ITERATE FOR EACH VERTICES
            for v, w in graph[u]: # ITERATE VIA EVERY NEIGHBOUR OF THE 'U' VERTEX
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: # IF THE WEIGHT OF U PLUS DISTANCE TO V IS SMALLER THEN THE CURRENT WEIGHT OF V UPDATE V
                    dist[v] = dist[u] + w
                    rep = False

        if _ == gr.getVertexCount() - 1 and not rep:  # THIS CHECKS FOR CYCLE IN THE GRAPH. IF IN THE LAST ITERATION THEIR
            # IS A CHANGE IN DISTANCE MATRIX THEN THERE IS A CYCLE IN THE GRAPG
            cycl = True
            print("the graph contain cycle")
            break

    if cycl:  # BREAKS IF THEIR IS A CYCLE IN THE GRAPH
        return

    print("Final result ")# PRINT THE FINAL RESULT
    print("{0}\t\t{1}".format("Destination", "No of Hops"))
    for i in dist.keys():
        print("{0}\t\t\t\t{1}".format(i, dist[i]))


# creating a graph object
g = Graph.Graph()

# Initializing grapg
g.addEdge('u', 'v', 3)
g.addEdge('u', 'x', 1)
g.addEdge('u', 'w', 7)
g.addEdge('v', 'w', 1)
g.addEdge('v', 'x', 1)
g.addEdge('x', 'w', 4)
g.addEdge('x', 'y', 2)
g.addEdge('w', 'z', 6)
g.addEdge('w', 'y', 5)
g.addEdge('y', 'z', 3)

# g.printGraph()  #printing Graph

# calling the Bellmanford Function
BellmanFord(g, g.getGraph(), 'u')
