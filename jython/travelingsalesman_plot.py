import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


## plot for MIMIC_travelingsalesman
travelingsalesmanDF = pd.read_csv(os.path.join('data', 'MIMIC-travelingsalesman.csv'))
sns.set_theme(style="whitegrid")

#fitness v. iters
plt.clf()
sns_plot=sns.lineplot(x="iters", y="fitness", data=travelingsalesmanDF,)
fig=sns_plot.get_figure()
fig.savefig(os.path.join('image', 'MIMIC_travelingsalesman_graph1.png'))

#fitness v. fevals
plt.clf()
sns_plot2=sns.lineplot(x="fevals", y="fitness", data=travelingsalesmanDF,)
fig2=sns_plot2.get_figure()
fig2.savefig(os.path.join('image', 'MIMIC_travelingsalesman_graph2.png'))

#fevals/iters v. fitness
plt.clf()
sns_plot3=sns.lineplot(x="fitness", y="value", hue="variable", data=pd.melt(travelingsalesmanDF, ['fitness']), legend="full")
fig3=sns_plot3.get_figure()
fig3.savefig(os.path.join('image', 'MIMIC_travelingsalesman_graph3.png'))

## plot for GA_travelingsalesman
travelingsalesmanDF = pd.read_csv(os.path.join('data', 'GA-travelingsalesman.csv'))
sns.set_theme(style="whitegrid")

#fitness v. iters
plt.clf()
sns_plot=sns.lineplot(x="iters", y="fitness", data=travelingsalesmanDF,)
fig4=sns_plot.get_figure()
fig4.savefig(os.path.join('image', 'GA_travelingsalesman_graph1.png'))

#fitness v. fevals
plt.clf()
sns_plot2=sns.lineplot(x="fevals", y="fitness", data=travelingsalesmanDF,)
fig5=sns_plot2.get_figure()
fig5.savefig(os.path.join('image', 'GA_travelingsalesman_graph2.png'))

#fevals/iters v. fitness
plt.clf()
sns_plot3=sns.lineplot(x="fitness", y="value", hue="variable", data=pd.melt(travelingsalesmanDF, ['fitness']), legend="full")
fig6=sns_plot3.get_figure()
fig6.savefig(os.path.join('image', 'GA_travelingsalesman_graph3.png'))


## plot for RHC_travelingsalesman
travelingsalesmanDF = pd.read_csv(os.path.join('data', 'RHC-travelingsalesman.csv'))
sns.set_theme(style="whitegrid")

#fitness v. iters
plt.clf()
sns_plot=sns.lineplot(x="iters", y="fitness", data=travelingsalesmanDF,)
fig7=sns_plot.get_figure()
fig7.savefig(os.path.join('image', 'RHC_travelingsalesman_graph1.png'))

#fitness v. fevals
plt.clf()
sns_plot2=sns.lineplot(x="fevals", y="fitness", data=travelingsalesmanDF,)
fig8=sns_plot2.get_figure()
fig8.savefig(os.path.join('image', 'RHC_travelingsalesman_graph2.png'))

#fevals/iters v. fitness
plt.clf()
sns_plot3=sns.lineplot(x="fitness", y="value", hue="variable", data=pd.melt(travelingsalesmanDF, ['fitness']), legend="full")
fig9=sns_plot3.get_figure()
fig9.savefig(os.path.join('image', 'RHC_travelingsalesman_graph3.png'))


## plot for SA_travelingsalesman
travelingsalesmanDF = pd.read_csv(os.path.join('data', 'SA-travelingsalesman.csv'))
sns.set_theme(style="whitegrid")

#fitness v. iters
plt.clf()
sns_plot=sns.lineplot(x="iters", y="fitness", data=travelingsalesmanDF,)
fig10=sns_plot.get_figure()
fig10.savefig(os.path.join('image', 'SA_travelingsalesman_graph1.png'))

#fitness v. fevals
plt.clf()
sns_plot2=sns.lineplot(x="fevals", y="fitness", data=travelingsalesmanDF,)
fig11=sns_plot2.get_figure()
fig11.savefig(os.path.join('image', 'SA_travelingsalesman_graph2.png'))

#fevals/iters v. fitness
plt.clf()
sns_plot3=sns.lineplot(x="fitness", y="value", hue="variable", data=pd.melt(travelingsalesmanDF, ['fitness']), legend="full")
fig12=sns_plot3.get_figure()
fig12.savefig(os.path.join('image', 'SA_travelingsalesman_graph3.png'))