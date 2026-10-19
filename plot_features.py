import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. 直接讀取本機資料夾中的 50_Startups.csv，避開網路 404 錯誤
dataset = pd.read_csv("50_Startups.csv")

# 2. 設定特徵與目標值，並進行 One-Hot Encoding（drop_first=True 避開虛擬變數陷阱，剛好得 5 個特徵）
X = dataset.drop('Profit', axis=1)
y = dataset['Profit']
X = pd.get_dummies(X, columns=['State'], drop_first=True)

feature_names = list(X.columns)

# 3. 循序前向特徵挑選 (1 到 5 個特徵)
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

# 4. 印出詳細評估結果表
print("=== 50-Startups 詳細評估結果表 ===")
print(f"{'Number of Features':<20} {'RMSE':<12} {'R-squared':<12} {'Selected Features'}")
for row in history:
    print(f"{row['num_features']:<20} {row['rmse']:<12.4f} {row['r2']:<12.4f} {row['features']}")

# 5. 繪製 1 到 5 個特徵的折線圖
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
plt.savefig('features_evaluation.png')
print("\n圖表已重新成功儲存為 features_evaluation.png！")