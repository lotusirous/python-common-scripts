import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# print(plt.style.available)
# Set global font settings

# # Say, "the default sans-serif font is COMIC SANS"
matplotlib.rcParams['font.sans-serif'] = "Arial Unicode MS"
# matplotlib.rcParams['font.size'] = 10.0
# # Then, "ALWAYS use sans-serif fonts"
# matplotlib.rcParams['font.family'] = "sans-serif"


aiodata = pd.Series(np.random.randn(50))

# print(aiodata['wait'])
fig, ax = plt.subplots()

ax.plot(aiodata, color='r', ls='--', linewidth=1.5, label='Proxied')


plt.title('Histogram of IQ')
ax.grid(True, linestyle=':')
ax.set_xlabel('Number of Requests')
ax.set_ylabel('Response time (ms)')
ax.legend(loc='upper right')
plt.show()
