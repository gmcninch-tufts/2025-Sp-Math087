import pandas as pd
import numpy as np

import json

rng = np.random.default_rng()

state = [ 'bull', 'bear', 'recess' ]

p = [ .6, .25, .15 ]

data = list(map(lambda x: str(x),rng.choice(state,p=p,size=20*52)))

def write_json(filename,data):
    with open(filename,'w') as f:
        json.dump(data,f,indent=3)


write_json('week09--data-market.json',list(map(lambda x: str(x),data)))




states = [ 'bull', 'bear', 'recess' ]

def get_next_week_probs(a,state):
    inds = get_indices(a,state)
    if (len(a)-1) in inds:
        n=len(inds)-1
    else:
        n=len(inds)
    N = len(a)

    # get the list of states for weeks following weeks of the input state
    nxt = { ns: [ i for i in inds if i+1<N and a[i+1] == st] for ns in states }
    
    return { nxt[ns]/n for ns in states }


pp = np.array([[0.80 , 0.15 , 0.25],
               [0.175, 0.80 , 0.25],
               [0.025, 0.05 , 0.50]])

def gen(pp,c):
    i = states.index(c)
    ps=pp[:,i]
    print(ps)
    return str(rng.choice(states,p=ps))

res = []
cur = str(rng.choice(states))
for _ in range(52*20):
    cur = gen(pp,cur)
    res.append(cur)


write_json('week09--data-market-new.json',list(map(lambda x: str(x),res)))
    
