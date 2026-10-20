# -*- coding: utf-8 -*-

# 讀取 index.html
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 定義陳煥老師要求的深入結果分析與討論 HTML 區塊
analysis_section = """
        <!-- 三、 結果分析與討論說明 (Analysis & Discussion) -->
        <div class="card" style="text-align: left; padding: 25px 30px; background-color: #ffffff; border-left: 5px solid #2b6cb0; margin-top: 25px;">
            <h3 style="color: #1a365d; margin-top: 0;">📝 50-Startups 迴歸結果深入分析與討論</h3>
            
            <h4 style="color: #2b6cb0; margin-bottom: 8px;">1. 特徵挑選與全域最佳模型（Parsimonious Principle）</h4>
            <p style="line-height: 1.7; font-size: 15px; margin-top: 0;">
                透過前向逐步挑選（Sequential Forward Selection, SFS）的迭代歷程：
            </p>
            <ul style="line-height: 1.8; font-size: 14.5px;">
                <li><strong>k = 1：</strong>僅選入 <code>R&D Spend</code>（研發支出）時，判定係數達 $R^2 = 0.9465$（RMSE: 8274.87），說明研發投入是影響獲利最關鍵之決定性變數。</li>
                <li><strong>k = 2（全域最佳模型）：</strong>納入 <code>Marketing Spend</code>（行銷支出）後，RMSE 降至全域最低點 <strong>8198.80</strong>，$R^2$ 升至最高峰 <strong>0.9474</strong>。此結果驗證了<strong>簡約原則（Ockham's Razor）</strong>：僅需「研發」與「行銷」兩大特徵，即可解釋超過 94.7% 的公司利潤變異。</li>
                <li><strong>k ≥ 3（過度擬合 Overfitting）：</strong>陸續加入州別與管理費用後，RMSE 反彈飆升至 9137.99，$R^2$ 跌至 0.9347。證明特徵並非越多越好，盲目加入無關特徵只會引入隨機噪聲，損害泛化能力。</li>
            </ul>

            <h4 style="color: #2b6cb0; margin-bottom: 8px; margin-top: 20px;">2. 類別變數與虛擬變數陷阱（Dummy Variable Trap）</h4>
            <p style="line-height: 1.7; font-size: 15px; margin-top: 0;">
                原始 <code>State</code> 包含三州，經 One-Hot Encoding 後嚴格執行 <code>drop_first=True</code> 捨棄 California 作為基準組。避免了自變數之間的完全共線性（Multicollinearity），確保矩陣 $(X^T X)^{-1}$ 可逆，符合回歸統計獨立性假設。
            </p>

            <h4 style="color: #2b6cb0; margin-bottom: 8px; margin-top: 20px;">3. 模型殘差診斷檢定（Residual Diagnostics）</h4>
            <p style="line-height: 1.7; font-size: 15px; margin-top: 0;">
                殘差散佈圖隨機均勻分佈於 0 兩側，符合<strong>同質變異性（Homoscedasticity）</strong>；殘差直方圖呈現對稱鐘形分佈並緊密貼合常態分佈曲線，通過<strong>誤差常態性（Normality of Errors）</strong>檢定。
            </p>

            <h4 style="color: #2b6cb0; margin-bottom: 8px; margin-top: 20px;">4. 商業決策啟示</h4>
            <p style="line-height: 1.7; font-size: 15px; margin-top: 0;">
                新創公司核心資金應高度集中於研發技術與市場行銷；行政管理花費與公司設立州別對公司獲利並無統計學上的顯著幫助。
            </p>
        </div>
"""

# 檢查是否已插入過
if "📝 50-Startups 迴歸結果深入分析與討論" not in content:
    # 尋找殘差圖的位置並插入在其後方
    marker = "model_residual_diagnostics.png"
    pos = content.find(marker)
    if pos != -1:
        end_tag = content.find("</div>", pos)
        content = content[:end_tag + 6] + "\n" + analysis_section + content[end_tag + 6:]
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ 成功：結果分析與討論已順利寫入 index.html！")
    else:
        print("❌ 找不到殘差圖位置，請確認檔案內容")
else:
    print("⚠️ 分析說明已經存在於 index.html 中，無需重複寫入！")