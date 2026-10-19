# 📊 多元線性回歸模型成果展 (Multiple Linear Regression Studio)

> **國立中興大學 人工智慧與資料科學碩士在職學位學程 (NCHU AI-DIC)**  
> **課程名稱：** 人工智慧與資訊安全 (7972)  
> **授課教授：** 陳煥 老師  
> **學號：** 5114050029  
> **學生姓名：** 陳枚君  
> **成果網頁 (GitHub Pages)：** [https://meimei1000103-dotcom.github.io/1019-DIC2/](https://meimei1000103-dotcom.github.io/1019-DIC2/)

---

## 📌 專案概述 (Overview)
本專案遵循資料科學標準方法論 **CRISP-DM** 流程，針對多元線性回歸進行特徵工程、循序前向特徵挑選 (SFS) 與回歸五大假設之殘差診斷：
1. **50-Startups 公司利潤預測**：4 特徵轉 5 維度後，經 SFS 挑選出最佳 2 特徵組合。
2. **Boston Housing 房價預測**：13 特徵評估與逐步挑選。
3. **HW2 Spotify Tracks 音樂流行度預測**：Kaggle 資料集（特徵數 15 個，符合 11 < 特徵數 < 30 之作業規範）。

---

## 🔬 核心方法與理論基礎 (Methodology)

### 1. 虛擬變數陷阱 (Dummy Variable Trap)
類別特徵經 One-Hot Encoding 後具備完全共線性，必須執行 `drop_first=True` 捨棄基準組，確保模型矩陣可逆且符合多元線性回歸獨立性假設。

### 2. 循序前向特徵挑選 (Sequential Forward Selection, SFS)
採用貪婪策略（Greedy Algorithm），每輪加入使驗證集 RMSE 最低、R² 最高的特徵，避免過度擬合（Overfitting）與維度災難。

### 3. 殘差診斷檢定 (Residual Diagnostics)
驗證經典回歸五大假設：
- **同質變異性 (Homoscedasticity)**：殘差均勻散佈於 0 的水平參考線兩側。
- **誤差常態性 (Normality of Errors)**：殘差直方圖呈現高斯常態分佈鐘形曲線。

---

## 📂 實驗成果摘要 (Results)

### 專案一：50-Startups 利潤預測
| 特徵數 (k) | 挑選特徵 | RMSE | R² Score | 模型狀態 |
| :---: | :--- | :---: | :---: | :--- |
| 1 | R&D Spend | 8274.52 | 0.9465 | 研發為最具影響力單一特徵 |
| **2** | **+ Marketing Spend** | **8198.24** | **0.9475** | **🌟 全域最佳組合** |
| 3 | + State_New York | 8311.20 | 0.9460 | 引入微量噪聲，輕度過度擬合 |
| 4 | + Administration | 8410.65 | 0.9447 | 管理費與利潤無顯著相關 |
| 5 | + State_Florida | 9150.12 | 0.9347 | 全特徵模型誤差顯著增加 |

### 專案二 (HW2)：Spotify Tracks 音樂流行度預測
- **規格合規**：選取 15 個聲學特徵（`danceability`, `energy`, `loudness`, `acousticness` 等），符合作業規範（$11 < \text{Features} < 30$）。
- **產出圖表**：`spotify_features_evaluation.png`（特徵評估折線圖）與 `spotify_residual_diagnostics.png`（殘差診斷分佈圖）。

---

## 🌐 互動網頁成果展
成果網頁部署於 GitHub Pages，支援以**下拉選單（Dropdown）**即時切換檢視 50-Startups、Spotify HW2 與 Boston Housing 三組資料集的評估折線圖與殘差圖。
