import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sb
import pandas as pd

a = sb.load_dataset("flights")
sb.relplot(x="passengers", y='month', hue="year", data=a)
