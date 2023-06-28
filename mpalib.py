import sys
import networkx as nx
import numpy as np

#finds all sources and sinks in the graph
def sources(g):
    s=[]
    for node in list(g):
        if len(nx.ancestors(g,node))==0:
            s.append(node)
    return s

def sinks(g):
    s=[]
    for node in list(g):
        if len(nx.descendants(g,node))==0:
            s.append(node)
    return s

def allsimplepaths(g, source=None):
    '''Finds all simple paths from a given set of source nodes. If no source is given, uses all source nodes from the graph g'''
    if source==None:
        source=sources(g)
    if type(source)!=list:
        source=[source]
    out=[]
    for src in source:
        for snk in sinks(g):
            paths=list(nx.all_simple_paths(g,src,snk))
            [out.append(p) for p in paths]
    return out

def unpackpath(path):
    '''Changes the path format from a generator to a list of tuples, each tuple representing a link present in the path.'''
    return [(path[i],path[i+1]) for i in range(len(path)-1)]

def spc(g):
    '''Returns the search path count weight for each link as a dictionary.'''
    weightdicts={}
    for p in allsimplepaths(g):
        for tup in unpackpath(p):
            if tup in weightdicts.keys():
                weightdicts[tup]+=1
            else:
                weightdicts[tup]=1
    return weightdicts

def pathweight(path, weights):
    out=0
    for link in unpackpath(path=path):
        out+=weights[link]
    return out

def main_path(g,source=None):
    if source==None:
        source=sources(g)

    mp=[]
    weights=spc(g)
    for src in source:
        ptwgts=[(path,pathweight(path,weights)) for path in allsimplepaths(g,src)]
        maxpath=sorted(ptwgts,key= lambda x: float(x[1]),reverse=True)[0]
        mp.append(maxpath[0])

    mainpath=nx.Graph()
    for p in mp:
        pt=unpackpath(p)
        for link in pt:
            u,v=link
            mainpath.add_edge(u,v)

    return mainpath