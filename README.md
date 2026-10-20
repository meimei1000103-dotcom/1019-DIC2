# 1019-DIC2: Interactive Feature Selection & Machine Learning Studio

[![Live Demo](https://img.shields.io/badge/LIVE%20DEMO-GITHUB%20PAGES-success?style=for-the-badge&logo=github)](https://meimei1000103-dotcom.github.io/1019-DIC2/)

🌐 **Live Demo 公開展示網址：**  
👉 [https://meimei1000103-dotcom.github.io/1019-DIC2/](https://meimei1000103-dotcom.github.io/1019-DIC2/)

---

## 📌 作業要求與實作亮點 (Highlights)

1. **互動式下拉選單 (Interactive Dropdown)**：
   在同一個 GitHub Pages 網頁中，透過 `<select>` 下拉選單即時動態切換檢視不同的迴歸分析資料集成果。
2. **50-Startups 利潤預測**：
   透過 One-Hot Encoding 與避免虛擬變數陷阱（`drop_first=True`），經前向逐步挑選（SFS）驗證最佳 2 特徵組合（`R&D Spend` + `Marketing Spend`）。
3. **HW2: Spotify Tracks Dataset (音樂流行度預測)**：
   - 符合作業規範：特徵數介於 11 到 30 個之間（本實作使用 15 個聲學特徵）。
   - 預測目標：`popularity`（0~100 分）。
   - 產出 SFS 迭代評估圖與殘差常態性診斷圖（Normality of Errors）。
4. **Boston Housing 房價預測**：
   整合 13 特徵逐步迴歸評估分析。

---

## 🔬 核心方法與理論 (Methodology)

- **CRISP-DM 流程**：遵循 Business/Data Understanding、Data Preparation、Modeling、Evaluation 到 Deployment 完整標準流程。
- **Dummy Variable Trap**：類別欄位編碼後捨棄基準組，確保模型矩陣可逆且無完全共線性。
- **Sequential Forward Selection (SFS)**：貪婪演算法迭代挑選，找出兼顧精簡性（Parsimonious）與最高解釋力（最低 RMSE、最高 $R^2$）之最佳子集。
- **殘差診斷 (Residual Diagnostics)**：檢驗迴歸五大假設之同質變異性（Homoscedasticity）與誤差常態分佈（Normality of Errors）。

---

## 📂 專案檔案清單

```text
.
├── index.html                         # 成果展示首頁 (含下拉選單切換資料集)
├── README.md                          # 專案詳細說明與 Live Demo 連結
├── 50_Startups.csv                    # 50-Startups 原始資料集
├── main.py / plot_features.py         # 50-Startups 迴歸分析與繪圖腳本
├── features_evaluation.png            # 50-Startups 特徵評估折線圖
├── model_residual_diagnostics.png     # 50-Startups 殘差診斷圖
├── hw2_spotify.py                     # HW2 Spotify 迴歸分析主程式
├── spotify_features_evaluation.png    # HW2 特徵數量評估折線圖
├── spotify_residual_diagnostics.png   # HW2 殘差診斷分佈圖
└── boston_regression.py               # Boston Housing 迴歸模型