import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from jedi.api.refactoring import inline

train=pd.read_csv('titanic_train.csv')
train.head()