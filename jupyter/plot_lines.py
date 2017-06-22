import pandas as pd 
import matplotlib
import matplotlib.pyplot as plt


# Set global font settings

# Say, "the default sans-serif font is COMIC SANS"
matplotlib.rcParams['font.sans-serif'] = "Droid Sans"
# Then, "ALWAYS use sans-serif fonts"
matplotlib.rcParams['font.family'] = "sans-serif"



aiodata = pd.read_csv('./aioproxy.tsv',delimiter='\t')
plaindata = pd.read_csv('./without_proxy.tsv',delimiter='\t')

print(aiodata['wait'])
fig, ax = plt.subplots()

ax.plot(aiodata['wait'], color='r',ls='--', linewidth=1.5, label='Proxied')
ax.plot(plaindata['wait'], linewidth=1.5, label='Original')

plt.title('Histogram of IQ')
ax.grid(True,linestyle=':')
ax.set_xlabel('Number of Requests')
ax.set_ylabel('Response time (ms)')
ax.legend(loc='left')
plt.show()

