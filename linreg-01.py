from scipy import stats

x = [1, 2, 3, 4, 5, 6]
y = [1, 3, 2, 5, 4, 5]

slope, intercept, r_value, p_value, std_error = stats.linregress(x,y)

print('Slope', slope)
print('Intercept', intercept)
print('R_value', r_value)
print('P_value', p_value)
print('Std_error', std_error)