import pandas as pd
import numpy as np
import seaborn as sb

x = pd.DataFrame({"Day": [1, 2, 3, 4], "Date": [11, 13, 17, 19]})
y = pd.DataFrame({"Day": [5, 6, 7, 8], "Date": [21, 10, 7, 29]})

mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
with sb.axes_style('white'):
    sb.jointplot(x=x, y=y, kind="kde", color='b')
