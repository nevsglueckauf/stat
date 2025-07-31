import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

diamonds = sns.load_dataset("diamonds")
print(diamonds['clarity'].unique())
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]

sns.boxenplot(
    diamonds, x="clarity", y="carat",
    color="b", order=clarity_ranking, width_method="linear",
)

plt.show()