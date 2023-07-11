import sys
import networkx as nx
import pandas as pd
import mpalib as mpa

#to do: create agents, greedy algortihm, each step the water level rises and they move higher according to the spc
#track and identify communities created by removing "lower" nodes
#should be object oriented?

class Agent:
    def __init__(self,id,pos) -> None:
        self.id=id
        self.pos=pos

    def get_pos(self):
        return self.pos

    def change_pos(self,pos):
        self.pos=pos

    def checkflooding():
        '''Check if neighbours are flooded'''
        pass

    def choosenextpos():
        '''greedy search'''
        pass

class Simulation:
    #data = dataframe(agent_ids,agent_pos,community)
    def __init__(self,waterlvl,data,g) -> None:
        self.waterlvl=waterlvl
        self.data=data
        self.g=g

    def create_agents(g):
        for node in list(g):
            node_citizen=Agent(node,node)
    
    def reiselvl():
        '''step function: increase waterlvl, check agents flooding, move agents, remove flooded links, check new communities,update data'''
        pass

    def end_sim():
        pass

    def floodlinks():
        pass

    def update():
        pass

    def check_new_community():
        pass

class NetworkxAdaptaaaaaa:
    pass