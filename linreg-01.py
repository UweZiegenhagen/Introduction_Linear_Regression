from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5, 6]
y = [50, 40, 45, 20, 25, 15]

# Calculation via stats module
slope, intercept, r_value, p_value, std_error = stats.linregress(x,y)

df = pd.DataFrame(np.transpose(np.array([x,y])), columns = ['x', 'y'])

print('Slope', slope)
print('Intercept', intercept)
print('R_value', r_value)
print('P_value', p_value)
print('Std_error', std_error)

# manual computation
mean_x = df.mean()[0]
mean_y = df.mean()[1]

df['x-mean_x'] = df['x'] - mean_x
df['y-mean_y'] = df['y'] - mean_y

df['(x-mean_x)(y-mean_y)'] = df['x-mean_x'] * df['y-mean_y']

df['(x-mean_x)^2'] = df['x-mean_x']**2

sum_xmeanxymeany = df['(x-mean_x)(y-mean_y)'].sum()
sum_xminusxsq = df['(x-mean_x)^2'].sum()

slope = sum_xmeanxymeany / sum_xminusxsq
intersect = mean_y - slope * mean_x

print(df, '\n\nSlope: ', slope, '\nIntersect: ', intersect)

# graphics
plt.scatter(x,y)