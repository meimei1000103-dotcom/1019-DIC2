import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import norm

# 1. 讀取 50-Startups 資料
dataset = pd.read_csv("50_Startups.csv")

# 2. 特徵與目標處理（使用最佳特徵組合：R&D Spend 與 Marketing Spend）
X = dataset[['R&D Spend', 'Marketing Spend']]
y = dataset['Profit']

# 3. 建立並訓練回歸模型
model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X)
residuals = y - predictions  # 計算殘差 (真實值 - 預測值)

# 4. 繪製殘差診斷圖
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# (左圖) Residuals vs Predicted Profit
ax1.scatter(predictions, residuals, color='#1f77b4', edgecolors='black', alpha=0.8)
ax1.axhline(0, color='black', linestyle='--', linewidth=1)
ax1.set_title('Residuals vs Predicted Profit', fontsize=12)
ax1.set_xlabel('Predicted Profit ($)', fontsize=10)
ax1.set_ylabel('Residual ($)', fontsize=10)
ax1.grid(True, linestyle=':', alpha=0.6)

# (右圖) Residual Distribution (紫色直方圖 + 常態分佈曲線)
n, bins, patches = ax2.hist(residuals, bins=6, color='#9b5de5', edgecolor='black', density=True, alpha=0.7)
mu, std = norm.fit(residuals)
xmin, xmax = ax2.get_xlim()
x_axis = np.linspace(xmin, xmax, 100)
p = norm.pdf(x_axis, mu, std)
ax2.plot(x_axis, p, color='#5c2d91', linewidth=2)
ax2.set_title('Residual Distribution', fontsize=12)
ax2.set_xlabel('Profit Residual', fontsize=10)
ax2.set_ylabel('Density', fontsize=10)
ax2.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('model_residual_diagnostics.png', dpi=300)
print("殘差診斷圖已成功儲存為 model_residual_diagnostics.png！")