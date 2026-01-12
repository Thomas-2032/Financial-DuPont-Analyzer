# Financial-DuPont-Analyzer 

本專案是一個基於 Python 的自動化財報分析工具，專門用於實作 **杜邦分析 (DuPont Analysis)**。透過整合 `yfinance` API，使用者可以快速拆解企業的 ROE（股東權益報酬率），藉此評估公司的獲利能力、資產效率與財務槓桿。

## 核心邏輯：三階段杜邦公式
本工具將 ROE 拆解為以下三個關鍵指標：

$$ROE = \text{淨利率} \times \text{總資產週轉率} \times \text{權益乘數}$$

## 技術棧 (Tech Stack)
- **Language**: Python
- **Data Analysis**: Pandas
- **Visualization**: Matplotlib
- **API**: Yahoo Finance (yfinance)
- **Environment**: Docker (Optional)

## 如何使用
1. **複製本專案**
   ```bash
   git clone [https://github.com/Thomas-2032/Financial-DuPont-Analyzer.git](https://github.com/Thomas-2032/Financial-DuPont-Analyzer.git) 