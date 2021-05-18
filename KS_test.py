from scipy import stats
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('broski1.csv')


dfp = pd.DataFrame(data={
    'vipadeniy': df['broski']})


dfp.plot.kde()
plt.show()

print(stats.kstest(dfp['vipadeniy'], 'norm', (dfp['vipadeniy'].mean(), dfp['vipadeniy'].std()), N=len(dfp['vipadeniy'])))
print(stats.kstest('norm', 'norm', N=1000))

