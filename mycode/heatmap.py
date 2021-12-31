import matplotlib.pyplot as plt
import seaborn as sns

# Run this, you will get the heatmap which shows the relationship between "priority" and "severity".
values =[[87,0,6,16,161],[363,8,57,353,88],[594,70,1039,92,23],[259,213,68,9,0],[2687,26,78,55,16]]
x_ticks = ['unspecified', 'low', 'medium','high','urgent']
y_ticks = ['urgent', 'high', 'medium','low','unspecified']
ax = sns.heatmap(values, xticklabels=x_ticks, yticklabels=y_ticks,cmap="Blues",annot=True,fmt="d",vmin=0,vmax=1200)

ax.set_xlabel('priority')
ax.set_ylabel('severity')
plt.show()
figure = ax.get_figure()

