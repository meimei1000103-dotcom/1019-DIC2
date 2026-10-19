import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. 改由穩定的 GitHub 來源載入 Boston Housing 資料集
data_url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
df = pd.read_csv(data_url)

# 特徵欄位與目標值 (medv 為預測目標房價)
X = df.drop('medv', axis=1)
y = df['medv']
feature_names = list(X.columns)

# 2. 循序前向特徵挑選 (Forward Selection)
selected_features = []
remaining_features = list(feature_names)
history = []

for k in range(1, len(feature_names) + 1):
    best_score = -float('inf')
    best_feature = None
    best_rmse = None
    
    for feat in remaining_features:
        current_features = selected_features + [feat]
        model = LinearRegression()
        model.fit(X[current_features], y)
        preds = model.predict(X[current_features])
        
        r2 = r2_score(y, preds)
        rmse = np.sqrt(mean_squared_error(y, preds))
        
        if r2 > best_score:
            best_score = r2
            best_feature = feat
            best_rmse = rmse
            
    selected_features.append(best_feature)
    remaining_features.remove(best_feature)
    history.append({
        'num_features': k,
        'features': list(selected_features),
        'rmse': best_rmse,
        'r2': best_score
    })

# 3. 印出詳細評估結果表
print("=== Boston Housing 詳細評估結果表 ===")
print(f"{'Number of Features':<20} {'RMSE':<12} {'R-squared':<12} {'Selected Features'}")
for row in history:
    print(f"{row['num_features']:<20} {row['rmse']:<12.4f} {row['r2']:<12.4f} {row['features']}")

# 4. 繪製並儲存評估折線圖
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

nums = [h['num_features'] for h in history]
rmses = [h['rmse'] for h in history]
r2s = [h['r2'] for h in history]

ax1.plot(nums, rmses, marker='o')
ax1.set_title('RMSE by Number of Features')
ax1.set_xlabel('Number of Features')
ax1.set_ylabel('RMSE')

ax2.plot(nums, r2s, marker='o')
ax2.set_title('R-squared by Number of Features')
ax2.set_xlabel('Number of Features')
ax2.set_ylabel('R-squared')

plt.tight_layout()
plt.savefig('boston_evaluation.png')
print("\n圖表已成功存為 boston_evaluation.png！")