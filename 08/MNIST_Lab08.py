# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from sklearn.neighbors import KNeighborsClassifier
import matplotlib
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
import numpy as np


# %%
mnist = fetch_openml('mnist_784')


# %%
mnist


# %%
mnist['data']


# %%
mnist['target']


# %%
x, y = mnist['data'].to_numpy(), mnist['target'].to_numpy()


# %%
#1D numpy array
x[1]


# %%
x.shape


# %%
y.shape


# %%


# %%
# Visualizing a single image
some_digit = x[36001]
# Reshape the Image to Plot
some_digit_re = some_digit.reshape(28, 28)


# %%
plt.imshow(some_digit_re)


# %%
# In binary format
plt.imshow(some_digit_re, cmap=matplotlib.cm.binary, interpolation='nearest')
plt.axis('off')


# %%
y[36000]


# %%
# train-test split
x_train, x_test = x[:60000], x[60000:]
y_train, y_test = y[:60000], y[60000:]


# %%
#shuffling the data
shuffle_index = np.random.permutation(60000)
x_train, y_train = x_train[shuffle_index], y_train[shuffle_index]

# %% [markdown]
# ## Creating 2 digit classifier

# %%
#convert values from string to integer
y_train = y_train.astype(np.int8)
y_test = y_test.astype(np.int8)
# choose only labels containing 2's
y_train_2 = (y_train == 2)
y_test_2 = (y_test == 2)


# %%


# %%
clf = KNeighborsClassifier()


# %%
clf.fit(x_train, y_train)


# %%
x_train.shape


# %%
y_train.shape


# %%
clf.predict([some_digit])


# %%
