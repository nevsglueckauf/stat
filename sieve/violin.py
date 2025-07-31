import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib # due to bug on MacOS

matplotlib.use('TkAgg') # due to bug on MacOS

sns.set_theme(style="dark")
plt.title(label='Tips')
# Load the example tips dataset
tips = sns.load_dataset("tips")
print(tips.head())
#exit()
# Draw a nested violinplot and split the violins for easier comparison
sns.violinplot(data=tips, x="day", y="total_bill", hue="smoker",
               split=True, inner="quart", fill=False,
               palette={"Yes": "g", "No": ".35"})

plt.show()