import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample Laptop Price Data
prices = [600, 750, 800, 850, 900, 950, 1000, 1200, 1300, 2500, 2800]
df = pd.DataFrame(prices, columns=['Price'])

# 1. Using Matplotlib
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.boxplot(df['Price'])
plt.title('Matplotlib Boxplot')

# 2. Using Seaborn (often looks cleaner)
plt.subplot(1, 2, 2)
sns.boxplot(x=df['Price'], color='skyblue')
plt.title('Seaborn Boxplot')

plt.show()
