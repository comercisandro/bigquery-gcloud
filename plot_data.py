import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ENVIRONMENT = "indoor"

df = pd.read_csv("datosBQ-8-8.csv")
df = df.rename(columns={"meters":"distance"})
df["environment"].replace({"in": "indoor", "out": "outdoor"}, inplace=True)

df = df[df.environment == ENVIRONMENT]

# experiments = ['X-h1.1',
#                'X-h1.2',
#                'X-h1.3',
#                'X-h1.4',
#                'X-h2.1',
#                'X-h2.2',
#                'X-h2.3',
#                'X-h2.4',
#                'X-h3.1',
#                'X-h3.2',
#                'X-h3.3',
#                'X-h3.4',
#                'X-v1.1',
#                'X-v1.2',
#                'X-v1.3',
#                'X-v1.4',
#                'X-v2.1',
#                'X-v2.2',
#                'X-v2.3',
#                'X-v2.4']
#
# df = df[df['experiment'].isin(experiments)]

# otros filtros
#df = df[(df.rx_label == "e") | (df.rx_label == "f") | (df.rx_label == "n")| (df.rx_label == "o")]
#df = df[(df.experiment == 'X-h1.1') | (df.experiment == 'X-h1.2') | (df.experiment == 'X-h1.3') | (df.experiment == 'X-h1.4')]

df = df.groupby(['environment', 'experiment', 'distance', 'rx_label', 'run'])['rssi'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10,6))
ax = sns.countplot(data=df, x="rx_label", hue="experiment")
plt.legend(bbox_to_anchor=(1.13, 1), loc='upper right')
plt.title(ENVIRONMENT.title() + ":" + " Experimentos por cada celular")
plt.savefig(ENVIRONMENT)