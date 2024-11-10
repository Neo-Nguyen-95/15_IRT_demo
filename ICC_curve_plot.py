import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %% IRT 1PL PLOT
# Generate data

theta = np.linspace(-4, 4, 100)
b = -1
a = 1
prob = 1 / (1 + np.exp(- a * (theta - b)))

# Plot
plt.figure(figsize=(6, 4))
sns.lineplot(x=theta, y=prob)

# Add reference lines
plt.axhline(0.5, color='gray', linestyle='--')
plt.axvline(-1, color='gray', linestyle='--')

# Labels
plt.xlabel("Năng lực của thí sinh")
plt.ylabel("Tỉ lệ trả lời đúng")

plt.show()

# %% IRT 2PL plot

theta = np.linspace(-4, 4, 100)

a1 = 1.1
b1 = 0.5

a2 = 1.5
b2 = -1.2

def prob(a, b, theta):
    return 1 / (1 + np.exp(- a * (theta - b)))

# Plot
plt.figure(figsize=(6, 4))
sns.lineplot(x=theta, y=prob(a2, b2, theta), label='Câu hỏi 1')
sns.lineplot(x=theta, y=prob(a1, b1, theta), label='Câu hỏi 2')
plt.axhline(0.5, color='gray', linestyle='--')
plt.axvline(0.5, color='gray', linestyle='--')
plt.axvline(-1.2, color='gray', linestyle='--')

# Labels
plt.xlabel("Năng lực của thí sinh")
plt.ylabel("Tỉ lệ trả lời đúng")

plt.legend()

plt.show()