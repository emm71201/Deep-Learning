#%%
import numpy as np
# %%
def predict(p, W, b):

    return int(np.dot(W, p) + b >= 0)
# %%
# let's limit do a simple case
def train(P, T):

    W = np.array([1,1])
    b = 0

    for i in range(len(P)):
        p = P[i]
        t = T[i]

        a = predict(p, W, b)
        W += (t-a) * p
        b += (t-a)

    return W, b
# %%
P = np.array([[1,4], [1,5], [2,4], [2,5], [3,1], [3,2], [4,1], [4,2]])
T = [0, 0, 0, 0, 1,1,1,1]
#%%
W,b = train(P[0:5],T[0:5])
for p in P:
    print(predict(p, W, b))
# %%
