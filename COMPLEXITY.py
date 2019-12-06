import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import os
"""1.1.1.1, 1.0.0.1, 8.8.8.8, 8.8.4.4, 192.168.1.1, 208.67.222.222, 208.67.220.220"""
class DIRS(object):
    def __init__(self):
        self.graph = nx.Graph()

    
    def findFolders(self, path):
        " ["","","",""] "
        paths = []
        if path[-1] == '/':
            everything = os.popen("ls -F "+path).read().split('\n')
            everything = everything[:-1]
            paths = filter(lambda var: True if var[-1] == '/' else False , everything)
        return  list(paths);
    
    def listDirs(self, path):
        "[{'path/':['','','']}]"
        paths = self.findFolders(path);
        res = [];
        for Subpath in paths:
            res.append({path+Subpath: self.findFolders(path+Subpath)})
        return res;
    
    def initGraph(self, path):
        folders = self.listDirs(path);
        for Folder in folders:
            self.graph.add_node(list(Folder.keys())[0]);
            for subFolder in Folder[list(Folder.keys())[0]]:
                self.initGraph(subFolder);
                self.graph.add_edge(list(Folder.keys())[0], subFolder);


Dir = DIRS();   
Dir.initGraph('/etc/');
G = Dir.graph
# nx.draw(G, with_labels=True, arrows=False)
# plt.show()

# nx.nx_agraph.write_dot(G,'test.dot')
# plt.title('dossier des ')

pos=graphviz_layout(G, prog='dot')
# nx.draw(G, pos, with_labels=True, arrows=False)
nx.draw(G, pos, with_labels=True, arrows=True)
plt.show()
