# -*- coding: utf-8 -*-
# @Time    : 2019-03-25 11:46 AM
# @Author  : jiuyang
# @File    : pandas_data.py

import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

v = np.random.randn(20)
tx = pd.Series(v)
tx.index = pd.date_range('2018-12-01', periods = 20, freq = "d")
print("tx", "-" * 20, "\n", tx)

# rm = tx.rolling(window = 5, center = False).mean()
# rm.plot()
# tx.plot()
# plt.show()