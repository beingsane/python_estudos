#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pdb

pdb.set_trace()

def pyramid1(n):
    for i in range(1, n+1): 
        print((str(i)+" ")*i)

pdb.run("pyramid1(4)")
print pdb.runeval("2+3")
pdb.runcall(pyramid1,7)


print "oioioi" 



