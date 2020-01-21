import numpy as np
import seaborn as sb

c = np.random.normal(loc=5, size=100, scale=2)
sb.distplot(c)
