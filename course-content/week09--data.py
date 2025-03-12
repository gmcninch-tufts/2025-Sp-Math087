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
    n = if (len(a)-1) in inds:
            len(inds)-1
        else:
            len(inds)
    N = len(a)

    # get the list of states for weeks following weeks of the input state
    nxt = { ns: [ i for i in inds if i+1<N and a[i+1] == st] for ns in states }
    
    return { nxt[ns]/n for ns in states }
