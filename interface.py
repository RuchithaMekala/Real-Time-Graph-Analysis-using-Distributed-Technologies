from neo4j import GraphDatabase

class Interface:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password), encrypted=False)
        self._driver.verify_connectivity()

    def close(self):
        self._driver.close()

    def bfs(self, start_node, last_node):
        # TODO: Implement this method
        with self._driver.session(database="neo4j") as session:
            graph_query = """CALL gds.graph.project('bfs','Location','TRIP')"""
            session.run(graph_query)
            bfs_query="""MATCH (a:Location), (b:Location)
            WHERE a.name = {} and b.name = {}
            CALL gds.bfs.stream('bfs',{{sourceNode: a, targetNodes: b}}) 
            YIELD path
            RETURN path""".format(start_node,last_node)
            res = session.run(bfs_query)
            delete_graph = """CALL gds.graph.drop('bfs')"""
            session.run(delete_graph)
            return res.data()

        #raise NotImplementedError

    def pagerank(self, max_iterations, weight_property):
        # TODO: Implement this method
        graph_name = 'pagerank'
        with self._driver.session(database="neo4j") as session:
            graph_query = """CALL gds.graph.project('{}','Location','TRIP',{{relationshipProperties:'{}'}});""".format(graph_name,weight_property)
            session.run(graph_query)
            pagerank_query = """CALL gds.pageRank.stream('{}', {{
        maxIterations: {},
        dampingFactor: 0.85,
        relationshipWeightProperty: '{}'}})
        YIELD nodeId, score
        RETURN gds.util.asNode(nodeId).name AS name, score 
        ORDER BY score DESC LIMIT 1
        UNION ALL 
        CALL gds.pageRank.stream('{}', {{
        maxIterations: {},
        dampingFactor: 0.85,
        relationshipWeightProperty: '{}'}})
        YIELD nodeId, score
        RETURN gds.util.asNode(nodeId).name AS name, score 
        ORDER BY score ASC LIMIT 1;""".format(graph_name, max_iterations, weight_property,graph_name, max_iterations, weight_property)
            pagerank_result = session.run(pagerank_query)
            #print(pagerank_result.data())
            #max_result = session.run(max_query)
            delete_graph_query = """CALL gds.graph.drop('{}')""".format(graph_name)
            session.run(delete_graph_query)
            return pagerank_result.data()
        #raise NotImplementedError

