import matplotlib.pyplot as plt
import seaborn as sns
# Ploting a Displot using displot function
# sns.displot([0, 0 ,0])
# plt.show()

# Plotting a Displot Without the Histogram
sns.displot([ -2,0, 1 , 2, 5 , 3], kind="kde")
plt.show()
