import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="darkgrid")
df = sns.load_dataset("penguins")
print(df.head())
sns.displot(
    df, x="flipper_length_mm", row="species", col="sex",
    binwidth=3, height=3, facet_kws=dict(margin_titles=True),
)

plt.show()