# -*- coding: utf-8 -*-

# @Time  : 2020/10/9 11:13

# @Author : zz

# @Project : zhanzge

# @FileName: test.py

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

import numpy as np
import sys
import networkx as nx
import matplotlib.pyplot as plt
from walker import *

g = nx.DiGraph()
g.add_edge(0, 1)

nx.draw(g, with_labels=True)
plt.show()
