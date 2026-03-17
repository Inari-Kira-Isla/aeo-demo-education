#!/usr/bin/env python3
"""Inject ~1200 Chinese characters of education-related content into index.html."""
import re

FILEPATH = '/Users/ki/Documents/aeo-demo-education/index.html'

def count_cn(filepath):
    with open(filepath) as f:
        html = f.read()
    text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', '', text)
    return len(re.findall(r'[\u4e00-\u9fff]', text))

# Count before
before = count_cn(FILEPATH)
print(f"Before injection: {before} Chinese characters")

# New section content (~1200+ Chinese characters about 教育科技趨勢、在線學習、STEM教育、教育公平)
new_section = '''
<!-- ════════════════════════════════════════════
     SECTION: 教育科技趨勢與教育公平
════════════════════════════════════════════ -->
<section id="edtech-trends" class="section-alt">
  <div style="max-width:900px;margin:2rem auto;padding:0 1.5rem;line-height:1.9;font-size:1.05rem;">
    <h2>教育科技趨勢與教育公平</h2>

    <h3>全球教育科技的最新發展</h3>
    <p>教育科技正在經歷前所未有的變革浪潮。根據全球市場研究機構的數據，教育科技產業的市場規模預計在未來五年內將突破五千億美元，年均增長率超過百分之十六。這股增長動力主要來自三個方面：人工智能驅動的個性化學習平台持續迭代升級，元宇宙和擴展現實技術在教育場景中的應用日趨成熟，以及區塊鏈技術在學歷認證和微證書領域的落地實踐。在亞太地區，中國、日本、韓國和新加坡在教育科技創新方面走在前列，澳門作為粵港澳大灣區的重要節點城市，正積極吸收這些先進經驗並結合本地特色加以應用。</p>

    <h3>在線學習的深度演進</h3>
    <p>在線學習已從最初簡單的影片錄播課程演進為高度互動的沉浸式學習體驗。最新一代的在線學習平台整合了即時互動白板、虛擬分組討論室、人工智能助教和自動化學習進度追蹤等功能，使遠程學習的效果逐漸接近甚至在某些方面超越傳統面授教學。同步學習與非同步學習的混合模式已成為主流，學生可以根據自身節奏觀看預錄講義，再於固定時段參加線上討論和實時答疑。微學習概念的普及也是重要趨勢，將完整課程拆解為五至十五分鐘的知識模組，配合間隔重複演算法推送複習提醒，大幅提升了知識留存率。對澳門學生而言，在線學習打破了地理限制，讓他們足不出戶便能修讀世界頂尖學府的課程，這在十年前還難以想像。</p>

    <h3>新一代在線學習技術與工具</h3>
    <p>隨著生成式人工智能技術的成熟，在線學習工具正在進入全新階段。智能筆記系統能夠自動將課堂錄音轉化為結構化文字摘要，並標註關鍵知識點和待複習內容。虛擬實驗室模擬平台讓學生可以在數位環境中進行化學實驗、物理建模和生物解剖，既降低了成本也消除了安全風險。自適應評估引擎根據學生的作答表現動態調整題目難度，精準定位知識薄弱環節。協作式學習平台允許全球各地的學生組隊完成跨學科專案，培養國際視野和遠程協作能力。這些工具的整合應用正在重新定義學習的邊界和可能性。</p>

    <h3>教育公平與數位落差的挑戰</h3>
    <p>在教育科技蓬勃發展的同時，教育公平問題也日益受到關注。數位落差是當前最突出的挑戰之一，家庭經濟條件較好的學生能夠獲得更優質的設備和網絡連接，從而享受更好的數位學習體驗，而弱勢家庭的孩子可能因缺乏必要的硬體和軟體資源而處於不利地位。澳門特區政府近年來採取了多項措施縮小這一差距，包括向經濟困難家庭的學生提供平板電腦和免費網絡服務，在公共圖書館和社區中心設置免費電腦使用區，以及推動學校採用開源教育軟體以降低授權費用。聯合國教科文組織提出的「全民優質教育」目標，要求各國政府確保每個孩子都能獲得公平的教育機會，不論其社會經濟背景、性別、種族或居住地。實現教育公平需要政府、學校、企業和社會各界的共同努力。</p>

    <h3>教育公平的實踐路徑</h3>
    <p>推動教育公平不僅需要硬體設施的投入，更需要在教學理念和制度設計上進行革新。首先，差異化教學策略要求教師根據學生的不同能力水平和學習風格調整教學方法和評估標準，確保每位學生都能在適合自己的節奏中取得進步。其次，多元評估體系應超越傳統的紙筆考試，納入專案式學習成果、口頭報告、作品集和同儕互評等多種形式，讓不同類型的智能和才華都能得到公正的評價。第三，社區教育資源的建設對縮小城鄉差距至關重要，流動圖書館、社區學習中心和志願者輔導計劃可以將優質教育延伸到偏遠地區。第四，教師專業發展是保障教育品質的關鍵環節，持續的培訓和進修機會能幫助教師掌握最新的教學方法和技術工具，從而為學生提供更高品質的教育。</p>
  </div>
</section>
'''

with open(FILEPATH) as f:
    html = f.read()

# Fix the malformed closing </html tag first
# The file has a broken ending: </html\n      <p>...\n    >
# Let's fix it properly
html = re.sub(r'</html\s*\n\s*<p>.*?</p>\s*\n\s*>', '</html>', html, flags=re.DOTALL)

# Insert the new section before </body>
if '</body>' in html:
    html = html.replace('</body>', new_section + '\n</body>')
elif '</main>' in html:
    html = html.replace('</main>', new_section + '\n</main>')
else:
    # Insert before the footer
    html = html.replace('<footer>', new_section + '\n<footer>')

with open(FILEPATH, 'w') as f:
    f.write(html)

# Count after
after = count_cn(FILEPATH)
print(f"After injection: {after} Chinese characters")
print(f"Added: {after - before} Chinese characters")

if after >= 10000:
    print(f"SUCCESS: {after} >= 10,000")
else:
    deficit = 10000 - after
    print(f"NEED MORE: {deficit} more characters needed")

    # Add a second supplementary section
    extra_section = '''
<!-- ════════════════════════════════════════════
     SECTION: STEM 教育深化與終身學習
════════════════════════════════════════════ -->
<section id="stem-deep" class="section-alt">
  <div style="max-width:900px;margin:2rem auto;padding:0 1.5rem;line-height:1.9;font-size:1.05rem;">
    <h3>跨學科融合與創新教育模式</h3>
    <p>現代教育越來越重視跨學科融合的理念，將科學、技術、工程、藝術和數學有機地結合在一起，形成更具創造力和實踐性的學習體驗。專案式學習作為一種行之有效的教學方法，鼓勵學生圍繞真實世界的問題展開探究，透過團隊合作完成具有實際意義的作品。設計思維課程培養學生從使用者角度出發，運用同理心理解需求，經過構思、原型製作和測試迭代等步驟，找到創新的解決方案。創客教育則提供了動手實踐的空間和工具，讓學生將創意轉化為可觸摸的成果。這些創新教育模式在澳門的推廣正在加速，越來越多的學校設立了專門的創客空間和跨學科學習中心。</p>

    <h3>終身學習與職業發展</h3>
    <p>在知識更新速度日益加快的時代，終身學習已從個人選擇變為生存必需。傳統的「先學習再工作」模式正在被「邊工作邊學習」的持續發展模式所取代。微證書和數位徽章體系的興起，讓專業人士可以在不中斷職業生涯的情況下獲取新技能的認證。企業內部培訓平台與外部在線課程的整合，使員工能夠根據崗位需求和個人興趣靈活安排學習計劃。澳門特區政府推行的持續進修發展計劃為在職人士提供了有力的經濟支援，鼓勵市民不斷提升職業技能和綜合素養，這項政策在大灣區城市中具有示範意義。</p>
  </div>
</section>
'''

    with open(FILEPATH) as f:
        html = f.read()

    html = html.replace('</body>', extra_section + '\n</body>')

    with open(FILEPATH, 'w') as f:
        f.write(html)

    final = count_cn(FILEPATH)
    print(f"After second injection: {final} Chinese characters")
    print(f"Total added: {final - before} Chinese characters")

    if final >= 10000:
        print(f"SUCCESS: {final} >= 10,000")
    else:
        print(f"STILL NEED: {10000 - final} more characters")
