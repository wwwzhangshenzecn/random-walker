# -*- coding: utf-8 -*-

# @Time  : 2020/10/9 10:47

# @Author : zz

# @Project : zhanzge

# @FileName: walker.py

# 著作权归作者所有。
'''

                .-~~~~~~~~~-._       _.-~~~~~~~~~-.
            __.'              ~.   .~              `.__
          .'//                  \./                  \\`.
        .'//                     |                     \\`.
      .'// .-~"""""""~~~~-._     |     _,-~~~~"""""""~-. \\`.
    .'//.-"                 `-.  |  .-'                 "-.\\`.
  .'//______.============-..   \ | /   ..-============.______\\`.
.'______________________________\|/______________________________`.

学海无涯 回头是岸
'''

import networkx as nx

class Walker:

    def __init__(self, graph: nx.DiGraph, startNodeList: list):
        '''

        :param graph: networkx.Digraph 有向图，带有边权重
        :param startNodeList: 游走的初始节点列表
        '''
        self.graph = graph
        self.startNodeList = startNodeList
        if graph.is_directed():
            self.sample_graph = nx.DiGraph()  # 根据初始节点游走后，最后的结果
        else:
            self.sample_graph = nx.Graph()

    def Random_Walker(self, deep=5, size = 1):
        '''
        # 根据初始列表进行速随机游走
        :return:
        '''
        for node in self.startNodeList:
            self.__walker(node, None, deep, size)

    def __walker(self, node, lastNode=None, deep = 5, size= 1, probilityKey='weight'):
        '''
        :param node: 目前游走的起始节点
        :param lastNode: 上一步的节点，防止重复
        :return: None
        '''
        if deep < 0:
            return
        probility_nodes = dict(self.graph.adj[node])
        probility_nodes.pop(lastNode,  None)
        if len(probility_nodes) == 0:
            return
        keys, probs = [], []
        sumPorb = 0.0
        for k, wv in probility_nodes.items():
            keys.append(k)
            probs.append(wv[probilityKey])
            sumPorb += wv[probilityKey]
        probs = [probs[i] / sumPorb for i in range(len(probs))]
        nextNode = np.random.choice(keys,size=size, p=probs)
        for n in set(nextNode):
            if nodes == 1 and n == 0:
                print(1)
            self.sample_graph.add_edge(node, n)
            self.__walker(n, node, deep-1, size)


if __name__=='__main__':
    import numpy as np
    import sys
    import networkx as nx
    import matplotlib.pyplot as plt

    g = nx.petersen_graph()
    nx.draw(g, with_labels=True)
    plt.show()
    print(len(g.edges))
    print(g.edges)

    edges = g.edges
    for (k, v) in edges:
        prob = np.random.randint(0, 100) / 100.0
        g.edges[(k, v)]['weight'] = prob
    nodes = [2, 5, 8]

    print(g.adj[8])

    rw = Walker(g, nodes)
    rw.Random_Walker(size=4, deep=2)
    sample = rw.sample_graph

    nx.draw(sample, with_labels=True)
    # plt.show()
    print(len(sample.edges))
    print(sample.edges)