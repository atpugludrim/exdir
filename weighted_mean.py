import numpy as np

d = np.arange(2*3*4).reshape(2,3,4,1)
w = np.arange(4)
#-----------------------  first way  -------------------------
print(f"{d = }\n{w.reshape(-1,1) = }")
print(f"{d*w.reshape(-1,1)=}")
print(f"{np.mean(np.sum(d*w.reshape(-1,1),axis=2))=}")

#----------------------  second way  -------------------------
d_ = np.transpose(d,(2,0,1,3))
print(f"{d_.shape=}")
d_ = d_.reshape(8, 3)
w_ = np.repeat(w, 2)
print(f"{d_=}")
print(f"{w_.reshape(-1,1)=}")
print(f"{d_*w_.reshape(-1,1)=}")
print(f"{np.mean(np.sum(d_*w_.reshape(-1,1),axis=1))=}")
print(f"{np.mean(np.sum(d*w.reshape(-1,1),axis=2))=}")
print(f"{np.sum(d_*w_.reshape(-1,1),axis=1)=}")
print(f"{np.sum(d*w.reshape(-1,1),axis=2).reshape(-1)=}")
