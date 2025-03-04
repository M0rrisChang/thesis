from scipy.optimize import leastsq
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np


sales = []
# china
# weekly
#exp_date_count = {4: 2173, 5: 14461, 6: 22966, 7: 30377, 8: 6602, 9: 2876, 10: 709}
# daily
#exp_date_count = {'2020-01-23': 259, '2020-01-24': 457, '2020-01-25': 688, '2020-01-26': 769, '2020-01-27': 1771, '2020-01-28': 1459, '2020-01-29': 1737, '2020-01-30': 1981, '2020-01-31': 2099, '2020-02-01': 2589, '2020-02-02': 2825, '2020-02-03': 3235, '2020-02-04': 3884, '2020-02-05': 3694, '2020-02-06': 3143, '2020-02-07': 3385, '2020-02-08': 2652, '2020-02-09': 2973, '2020-02-10': 2467, '2020-02-11': 2015, '2020-02-12': 14108, '2020-02-13': 5090, '2020-02-14': 2641, '2020-02-15': 2008, '2020-02-16': 2048, '2020-02-17': 1888, '2020-02-18': 1749, '2020-02-19': 391, '2020-02-20': 889, '2020-02-21': 823, '2020-02-22': 648, '2020-02-23': 214, '2020-02-24': 508, '2020-02-25': 406, '2020-02-26': 433, '2020-02-27': 327, '2020-02-28': 427, '2020-02-29': 573, '2020-03-01': 202, '2020-03-02': 125, '2020-03-03': 119, '2020-03-04': 139, '2020-03-05': 143, '2020-03-06': 99, '2020-03-07': 44, '2020-03-08': 40, '2020-03-09': 19, '2020-03-10': 24, '2020-03-11': 15, '2020-03-12': 20, '2020-03-13': 11, '2020-03-14': 20, '2020-03-15': 16, '2020-03-16': 21, '2020-03-17': 13, '2020-03-18': 34}

# US
# weekly
#exp_date_count = {4: 4, 5: 3, 6: 4, 7: 3, 8: 20, 9: 41, 10: 461, 11: 2962, 12: 30247, 13: 107140, 14: 102567}
# daily
#exp_date_count = {'2020-03-02': 25, '2020-03-03': 21, '2020-03-04': 31, '2020-03-05': 68, '2020-03-06': 57, '2020-03-07': 139, '2020-03-08': 120, '2020-03-09': 68, '2020-03-10': 354, '2020-03-11': 322, '2020-03-12': 382, '2020-03-13': 516, '2020-03-14': 547, '2020-03-15': 773, '2020-03-16': 1133, '2020-03-17': 1789, '2020-03-18': 1365, '2020-03-19': 5894, '2020-03-20': 5421, '2020-03-21': 6392, '2020-03-22': 8253, '2020-03-23': 9921, '2020-03-24': 10073, '2020-03-25': 12038, '2020-03-26': 18058, '2020-03-27': 17821, '2020-03-28': 19821, '2020-03-29': 19408, '2020-03-30': 20921, '2020-03-31': 26365, '2020-04-01': 25200, '2020-04-02': 30081}

# UK
# weekly
#exp_date_count = {11: 1144, 12: 4597, 13: 14039, 14: 14393}
# daily
#exp_date_count = {'2020-03-16': 407, '2020-03-17': 409, '2020-03-18': 682, '2020-03-19': 74, '2020-03-20': 1298, '2020-03-21': 1053, '2020-03-22': 674, '2020-03-23': 985, '2020-03-24': 1438, '2020-03-25': 1476, '2020-03-26': 2172, '2020-03-27': 2933, '2020-03-28': 2567, '2020-03-29': 2468, '2020-03-30': 2673, '2020-03-31': 3028, '2020-04-01': 4384, '2020-04-02': 4308}

# TW
# weekly
#exp_date_count = {11: 14, 12: 110, 13: 129, 14: 41}
# daily
exp_date_count = {'2020-03-11': 1, '2020-03-12': 1, '2020-03-13': 1, '2020-03-14': 3, '2020-03-15': 6, '2020-03-16': 8, '2020-03-17': 10, '2020-03-18': 23, '2020-03-19': 8, '2020-03-20': 27, '2020-03-21': 18, '2020-03-22': 16, '2020-03-23': 26, '2020-03-24': 20, '2020-03-25': 20, '2020-03-26': 17, '2020-03-27': 15, '2020-03-28': 16, '2020-03-29': 15, '2020-03-30': 8, '2020-03-31': 16, '2020-04-01': 7, '2020-04-02': 10}

for k, v in exp_date_count.items():
    sales.append(v)

print('sum M', sum(sales))


# sales vector
#sales = [840, 1470, 2110, 4000, 7590, 10950, 10530, 9470, 7790, 5890, 4500, 6900, 3000]
sales = np.array(sales)
#sales = np.array(sales)
#time intervals
t = np.linspace(1.0, float(len(sales)), num=len(sales))
# cumulatice sales
c_sales = np.cumsum(sales)
# initial variables(M, P & Q)
vars = [sum(sales), 0.0038, 0.2]

# residual (error) function
def residual(vars, t, sales):
    M = vars[0]
    P = vars[1]
    Q = vars[2]
    Bass = M * (((P + Q) ** 2 / P) * np.exp(-(P + Q) * t)) / (1 + (Q / P) * np.exp(-(P + Q) * t)) ** 2
    return (Bass - (sales))
                 
# non linear least square fitting
varfinal, success = leastsq(residual, vars, args=(t, sales))

# estimated coefficients
m = varfinal[0]
p = varfinal[1]
q = varfinal[2]


print(varfinal)
#sales plot (pdf)
#time interpolation
tp = (np.linspace(1.0, float(len(sales)) * 70, num=len(sales) * 70)) / 70
cofactor = np.exp(-(p + q) * tp)
sales_pdf = m * (((p + q) ** 2 / p) * cofactor) / (1 + (q / p) * cofactor) ** 2
plt.plot(tp, sales_pdf, t, sales)
plt.title('Keywords pdf')
plt.legend(['Fit', 'True'])
plt.show()


# Cumulative sales (cdf)
sales_cdf = m * (1 - cofactor) / (1 + (q / p) * cofactor)
plt.plot(tp, sales_cdf, t, c_sales)
plt.title('Keywords cdf')
plt.legend(['Fit', 'True'])
plt.show()
