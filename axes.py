import pandas as pd
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(12, 8))
ax=fig.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], marker='o', color='b', label='Sales')
ax.set_title('Sales Over Time')
ax.set_xlabel('Time')
ax.set_ylabel('Sales')
ax.legend() 
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()