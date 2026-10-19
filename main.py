import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# 1. 從 GitHub Gist 載入資料
url = "https://gist.githubusercontent.com/GaneshSparkz/b5662effbdae8746f7f7d8ed70c42b2d/raw/50_Startups.csv"
dataset = pd.read_csv(url)

print("--- 資料前五筆預覽 ---")
print(dataset.head(), "\n")

# 2. 定義自變數 (X) 與 應變數 (y)
# X 包含：'R&D Spend', 'Administration', 'Marketing Spend', 'State'
X = dataset.drop('Profit', axis=1) 
# y 是我們要預測的目標：'Profit'
y = dataset['Profit']

# 3. 處理類別變數 (One-Hot Encoding)
# 將 'State' 欄位（字串）轉換為虛擬變數 (Dummy Variables)
# drop_first=True 是為了避免「虛擬變數陷阱 (Dummy Variable Trap)」(完全共線性問題)
X = pd.get_dummies(X, columns=['State'], drop_first=True)

# 4. 切分訓練集與測試集 (80% 訓練, 20% 測試)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. 建立並訓練多元線性回歸模型
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# 印出模型學習到的權重 (係數) 與截距
print("--- 模型參數 ---")
print("截距 (Intercept):", regressor.intercept_)
coefficients = pd.DataFrame({'特徵 (Feature)': X.columns, '權重係數 (Coefficient)': regressor.coef_})
print(coefficients, "\n")

# 6. 利用測試集進行預測
y_pred = regressor.predict(X_test)

# 將真實值與預測值放在一起比較
comparison = pd.DataFrame({'真實利潤 (Actual)': y_test, '預測利潤 (Predicted)': y_pred})
print("--- 測試集預測結果比較 ---")
print(comparison, "\n")

# 7. 模型效能評估
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("--- 模型評估指標 ---")
print(f"R平方分數 (R-squared): {r2:.4f}")
print(f"平均絕對誤差 (MAE): {mae:.2f}")
