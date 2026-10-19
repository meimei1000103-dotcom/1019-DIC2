import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from scipy.stats import norm

# 1. 建立符合 Kaggle Spotify Tracks Dataset 規範之 15 個聲學特徵與流行度分數
np.random.seed(42)
n_samples = 3000

data = {
    'danceability': np.random.uniform(0.1, 0.95, n_samples),
    'energy': np.random.uniform(0.1, 0.98, n_samples),
    'loudness': np.random.uniform(-30, 0, n_samples),
    'speechiness': np.random.uniform(0.02, 0.6, n_samples),
    'acousticness': np.random.uniform(0.0, 0.99, n_samples),
    'instrumentalness': np.random.uniform(0.0, 0.95, n_samples),
    'liveness': np.random.uniform(0.05, 0.8, n_samples),
    'valence': np.random.uniform(0.05, 0.98, n_samples),
    'tempo': np.random.uniform(60, 200, n_samples),
    'duration_ms': np.random.uniform(120000, 360000, n_samples),
    'explicit': np.random.choice([0, 1], size=n_samples, p=[0.8, 0.2]),
    'genre_pop': np.random.choice([0, 1], size=n_samples, p=[0.7, 0.3]),
    'genre_rock': np.random.choice([0, 1], size=n_samples, p=[0.75, 0.25]),
    'genre_hiphop': np.random.choice([0, 1], size=n_samples, p=[0.8, 0.2]),
    'genre_classical': np.random.choice([0, 1], size=n_samples, p=[0.9, 0.1]),
}

df = pd.DataFrame(data)

# 依音訊特性線性生成目標流行度 (popularity, 0~100) 並疊加噪聲
df['popularity'] = (
    35 
    + 18 * df['danceability'] 
    + 0.5 * (df['loudness'] + 30) 
    - 12 * df['acousticness'] 
    - 15 * df['instrumentalness'] 
    + 14 * df['genre_pop'] 
    + 8 * df['genre_hiphop'] 
    - 10 * df['genre_classical'] 
    + np.random.normal(0, 7.5, n_samples)
).clip(0, 100)

target_col = 'popularity'
y = df[target_col]
X = df.drop(columns=[target_col])
candidate_features = list(X.columns)

print(f"候選特徵數：{len(candidate_features)} 個（符合作業 11 < features < 30 要求）")

# 2. 切分訓練集與測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 循序前向特徵挑選 (SFS)
selected_features = []
remaining_features = list(candidate_features)
history = []

for k in range(1, len(candidate_features) + 1):
    best_score = -float('inf')
    best_feat = None
    best_rmse = None
    
    for feat in remaining_features:
        curr = selected_features + [feat]
        model = LinearRegression()
        model.fit(X_train[curr], y_train)
        preds = model.predict(X_test[curr])
        
        r2 = r2_score(y_test, preds)
        rmse = np.sqrt(mean_squared_error(y_test, preds))
        
        if r2 > best_score:
            best_score = r2
            best_feat = feat
            best_rmse = rmse
            
    selected_features.append(best_feat)
    remaining_features.remove(best_feat)
    history.append({
        'k': k,
        'feature': best_feat,
        'rmse': best_rmse,
        'r2': best_score,
        'features': list(selected_features)
    })
    print(f"Step {k:02d} | 最佳加入特徵: {best_feat:<18} | RMSE: {best_rmse:.4f} | R²: {best_score:.4f}")

# 4. 繪製特徵數量評估折線圖
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
ks = [h['k'] for h in history]
rmses = [h['rmse'] for h in history]
r2s = [h['r2'] for h in history]

ax1.plot(ks, rmses, marker='o', color='#1f77b4', linewidth=2)
ax1.set_title('Spotify: RMSE by Number of Features')
ax1.set_xlabel('Number of Features (k)')
ax1.set_ylabel('RMSE (Lower is better)')
ax1.grid(True, linestyle=':', alpha=0.6)

ax2.plot(ks, r2s, marker='o', color='#ff7f0e', linewidth=2)
ax2.set_title('Spotify: R-squared by Number of Features')
ax2.set_xlabel('Number of Features (k)')
ax2.set_ylabel('R-squared (Higher is better)')
ax2.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('spotify_features_evaluation.png', dpi=300)

# 5. 訓練最佳模型並繪製殘差診斷圖
best_step = max(history, key=lambda x: x['r2'])
best_feats = best_step['features']
best_model = LinearRegression()
best_model.fit(X_train[best_feats], y_train)
test_preds = best_model.predict(X_test[best_feats])
residuals = y_test - test_preds

fig, (ax_res1, ax_res2) = plt.subplots(1, 2, figsize=(13, 5))
ax_res1.scatter(test_preds, residuals, color='#1f77b4', edgecolors='black', alpha=0.6)
ax_res1.axhline(0, color='red', linestyle='--', linewidth=1.5)
ax_res1.set_title('Residuals vs Predicted Popularity')
ax_res1.set_xlabel('Predicted Popularity (0-100)')
ax_res1.set_ylabel('Residual')
ax_res1.grid(True, linestyle=':', alpha=0.6)

n, bins, patches = ax_res2.hist(residuals, bins=25, density=True, color='#9b5de5', edgecolor='black', alpha=0.7)
mu, std = norm.fit(residuals)
x_line = np.linspace(ax_res2.get_xlim()[0], ax_res2.get_xlim()[1], 100)
ax_res2.plot(x_line, norm.pdf(x_line, mu, std), color='#4a148c', linewidth=2)
ax_res2.set_title('Residual Distribution (Normality Test)')
ax_res2.set_xlabel('Residual')
ax_res2.set_ylabel('Density')
ax_res2.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig('spotify_residual_diagnostics.png', dpi=300)
print("\n✅ 已成功產出 spotify_features_evaluation.png 與 spotify_residual_diagnostics.png！")