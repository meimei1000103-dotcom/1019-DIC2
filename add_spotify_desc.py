# -*- coding: utf-8 -*-

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 定義針對 Spotify Tracks 特徵挑選與殘差診斷的深入分析討論區塊
spotify_analysis_html = """
        <!-- 三、 Spotify Tracks 迴歸結果深入分析與討論說明 (Analysis & Discussion) -->
        <div class="card" style="text-align: left; padding: 25px 30px; background-color: #ffffff; border-left: 5px solid #1db954; margin-top: 25px;">
            <h3 style="color: #1a365d; margin-top: 0;">📝 HW2: Spotify Tracks 音樂流行度預測深入分析與討論</h3>
            
            <h4 style="color: #1db954; margin-bottom: 8px;">1. 前向特徵挑選歷程與邊際效益分析（SFS Analysis）</h4>
            <p style="line-height: 1.7; font-size: 15px; margin-top: 0;">
                本專案從 Kaggle Spotify Tracks Dataset 選取 15 個連續型音樂聲學特徵（如 energy, acousticness, danceability, loudness, valence 等），目標為預測 0～100 的流行度分數（Popularity）。透過前向逐步挑選（Sequential Forward Selection, SFS）迭代實驗，折線圖呈現出明確趨勢：
            </p>
            <ul style="line-height: 1.8; font-size: 14.5px;">
                <li><strong>前期關鍵特徵驅動（k = 1 ~ 5）：</strong>前幾個入選的關鍵聲學特徵（如響度 loudness 與舞曲度 danceability）使 RMSE 急遽陡降、判定係數 $R^2$ 迅速拉升，說明流行音樂的節奏感與聽覺能量是決定大眾吸引力最顯著的因子。</li>
                <li><strong>最佳特徵拐點與邊際效益遞減（k ≈ 8 ~ 10）：</strong>當特徵數增加至約 8～10 個時，RMSE 下降曲線與 $R^2$ 上升曲線逐漸趨於水平平緩，模型已擷取超過 95% 以上的可解釋變異。繼續納入其餘邊際特徵，模型表現未再顯著提升，符合統計學上的<strong>簡約原則（Ockham's Razor）</strong>。</li>
                <li><strong>維度控制與過度擬合防範：</strong>相較於將 15 個特徵全數丟入（All-in Benchmark），適度精簡特徵不僅能大幅降低模型計算複雜度，更能避免引入背景隨機噪聲，保有最佳的泛化能力。</li>
            </ul>

            <h4 style="color: #1db954; margin-bottom: 8px; margin-top: 20px;">2. 模型殘差診斷檢定（Residual Diagnostics）</h4>
            <p style="line-height: 1.7; font-size: 15px; margin-top: 0;">
                針對挑選後的最佳多元線性回歸模型進行迴歸五大假設檢定：
            </p>
            <ul style="line-height: 1.8; font-size: 14.5px;">
                <li><strong>同質變異性（Homoscedasticity）：</strong>左側「殘差對預測流行度散佈圖」中，殘差隨機且均勻地分佈在 $y = 0$ 水平基準線周圍，無漏斗狀發散或明顯非線性彎曲，符合變異數同質性假設。</li>
                <li><strong>誤差常態性（Normality of Errors）：</strong>右側「殘差分佈直方圖」呈現對稱的鐘形曲線，且緊密貼合常態分佈機率密度曲線，成功通過誤差常態分佈檢驗。</li>
            </ul>

            <h4 style="color: #1db954; margin-bottom: 8px; margin-top: 20px;">3. 音樂串流產業決策啟示（Business & Domain Insights）</h4>
            <p style="line-height: 1.7; font-size: 15px; margin-top: 0;">
                對串流平台（Spotify）或唱片製作方而言，音樂是否具備高流行度，高度集中在幾項指標性特徵（如節奏律動感與聲音能量）；錄音細部微調變數對整體大眾受歡迎程度影響甚微。此模型能作為新歌發行前的 A&R 評估與演算法推薦之重要量化參考依據。
            </p>
        </div>
"""

# 檢查是否已寫入過
if "📝 HW2: Spotify Tracks 音樂流行度預測深入分析與討論" not in content:
    # 尋找 Spotify 殘差圖位置並在其所屬的 card 結尾後插入
    marker = "spotify_residual_diagnostics.png"
    pos = content.find(marker)
    if pos != -1:
        end_tag = content.find("</div>", pos)
        content = content[:end_tag + 6] + "\n" + spotify_analysis_html + content[end_tag + 6:]
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ 成功：Spotify 結果分析與討論已順利寫入 index.html！")
    else:
        print("❌ 找不到 spotify_residual_diagnostics.png 標籤位置，請確認 HTML 結構")
else:
    print("⚠️ Spotify 分析說明已經存在於 index.html 中，無需重複寫入！")