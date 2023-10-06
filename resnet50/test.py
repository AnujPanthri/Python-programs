import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0.0001,1,0.01)
y=np.log(x)
plt.plot(x,y)
plt.plot(x,y,"rx")
plt.xlabel("value")
plt.ylabel("log value")
plt.show()

# # x=np.array([0.1,0.2,0.7])
# x=np.array([0.1,0.4,0.5])

# y=np.log(x) # makes low probabilty expand and high probability close
# print("x:",x)
# print("y:",y)


# def sample(preds, temperature=1.0):
#     # helper function to sample an index from a probability array
#     preds = np.asarray(preds).astype("float64")
#     preds = np.log(preds) / temperature
#     exp_preds = np.exp(preds)
#     preds = exp_preds / np.sum(exp_preds)
#     probas = np.random.multinomial(1, preds, 1)
#     return np.argmax(probas)