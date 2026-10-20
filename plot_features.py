import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. 讀取本機 50_Startups.csv 資料集
dataset = pd.read_csv("50_Startups.csv")

# 2. 設定特徵與預測目標，類別欄位 One-Hot Encoding (drop_first=True 避免虛擬變數陷阱)
X = dataset.drop('Profit', axis=1)
y = dataset['Profit']
X = pd.get_dummies(X, columns=['State'], drop_first=True)

feature_names = list(X.columns)

# 3. 切分訓練集與測試集 (80% 訓練, 20% 測試, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 4. 循序前向特徵挑選 (Sequential Forward Selection, 1 到 5 個特徵)
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
        model.fit(X_train[current_features], y_train)
        preds = model.predict(X_test[current_features])
        
        r2 = r2_score(y_test, preds)
        rmse = np.sqrt(mean_squared_error(y_test, preds))
        
        if r2 > best_score:
            best_score = r2
            best_feature = feat
            best_rmse = rmse
            
    selected_features.append(best_feature)
    remaining_features.remove(best_feature)
    history.append({
        'num_features': float(k),
        'features': list(selected_features),
        'rmse': best_rmse,
        'r2': best_score
    })

# 5. 印出詳細評估結果表
print("=== 50-Startups 詳細評估結果表 ===")
print(f"{'Number of Features':<20} {'Selected Features':<55} {'RMSE':<12} {'R-squared':<12}")
for row in history:
    print(f"{int(row['num_features']):<20} {str(row['features']):<55} {row['rmse']:<12.4f} {row['r2']:<12.4f}")

# 6. 繪製特徵數量評估折線圖 (完全吻合老師作業規格)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.8))

nums = [h['num_features'] for h in history]
rmses = [h['rmse'] for h in history]
r2s = [h['r2'] for h in history]

# 左圖：RMSE by Number of Features
ax1.plot(nums, rmses, marker='o')
ax1.set_title('RMSE by Number of Features', fontsize=10)
ax1.set_xlabel('Number of Features', fontsize=8)
ax1.set_ylabel('RMSE', fontsize=8)
ax1.tick_params(axis='both', labelsize=8)

# 右圖：R-squared by Number of Features
ax2.plot(nums, r2s, marker='o')
ax2.set_title('R-squared by Number of Features', fontsize=10)
ax2.set_xlabel('Number of Features', fontsize=8)
ax2.set_ylabel('R-squared', fontsize=8)
ax2.tick_params(axis='both', labelsize=8)

plt.tight_layout()
plt.savefig('features_evaluation.png', dpi=300)
print("\n圖表已重新成功儲存為 features_evaluation.png！")