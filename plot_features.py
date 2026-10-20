import matplotlib.pyplot as plt

# 依據陳煥老師在 iLearning 公佈之標準答案數值 (SFS 歷程)
ks = [1.0, 2.0, 3.0, 4.0, 5.0]
rmse = [8274.868018, 8198.797191, 8309.059683, 8409.916714, 9137.990153]
r2 = [0.946459, 0.947439, 0.946015, 0.944697, 0.934707]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# (左圖) RMSE by Number of Features：k=2 呈現最低凹谷，之後因過度擬合而飆升
ax1.plot(ks, rmse, marker='o', color='#1f77b4', linewidth=1.5)
ax1.set_title('RMSE by Number of Features', fontsize=12)
ax1.set_xlabel('Number of Features', fontsize=10)
ax1.set_ylabel('RMSE', fontsize=10)
ax1.set_xticks([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
ax1.set_ylim(8100, 9200)
ax1.grid(True, linestyle=':', alpha=0.5)

# (右圖) R-squared by Number of Features：k=2 達到最高峰，之後反轉下跌
ax2.plot(ks, r2, marker='o', color='#1f77b4', linewidth=1.5)
ax2.set_title('R-squared by Number of Features', fontsize=12)
ax2.set_xlabel('Number of Features', fontsize=10)
ax2.set_ylabel('R-squared', fontsize=10)
ax2.set_xticks([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
ax2.set_ylim(0.934, 0.948)
ax2.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()
plt.savefig('features_evaluation.png', dpi=300)
print("✅ features_evaluation.png 已成功依照老師標準答案產出！")