# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml

data = fetch_openml(name='wine', version=1, as_frame=True)
print(data.DESCR)
df = data.frame

df.sample(5)
df.describe()
df.dtypes

features = list(df.columns)
print("Available features:", features)
selected_features = [features[0], features[2], features[1], features[10], features[7]]
print("Selected features: ", selected_features)

fig, axs  = plt.subplots(1, len(selected_features), figsize = (20,3))

for ax, f in zip(axs, selected_features):
    ax.hist(df[f], bins=5, color='skyblue', edgecolor='black')
    ax.set_xlabel(f)
  
x = df[selected_features[3]]
y = df[selected_features[4]]

plt.scatter(x, y)
plt.xlabel(selected_features[4])
plt.ylabel(selected_features[3])
plt.show()


reference_feature = selected_features[3]  # The reference feature
comparison_feature = selected_features[4]  # A feature to compare to

# Create a scatter plot for the selected pair
plt.figure(figsize=(3, 4))
plt.scatter(df[reference_feature], df[comparison_feature], alpha=0.6)
plt.xlabel(reference_feature)
plt.ylabel(comparison_feature)

# Save the plot as an image file
plt.savefig('correlation_plot.png')

plt.show()
