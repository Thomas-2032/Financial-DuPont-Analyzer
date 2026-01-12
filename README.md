# Financial-DuPont-Analyzer 

本專案是一個基於 Python 的自動化財報分析工具，專門用於實作 **杜邦分析 (DuPont Analysis)**。透過整合 `yfinance` API，使用者可以快速拆解企業的 ROE（股東權益報酬率），藉此評估公司的獲利能力、資產效率與財務槓桿。

## 核心邏輯：三階段杜邦公式
本工具將 ROE 拆解為以下三個關鍵指標：

$$ROE = \text{淨利率} \times \text{總資產週轉率} \times \text{權益乘數}$$

## 技術棧
- **Language**: Python
- **Data Analysis**: Pandas
- **Visualization**: Matplotlib
- **API**: Yahoo Finance (yfinance)
- **Environment**: Docker (Optional)

## 功能特點
- **自動化數據抓取**：整合 `yfinance` API，輸入股票代號即可獲取最新財報數據。
- **杜邦分析建模**：自動拆解 ROE 為淨利率、資產週轉率與權益乘數。
- **自動化目錄管理**：程式會自動檢查並建立 `output/` 資料夾，無需手動配置。
- **視覺化報告產出**：自動生成高解析度的分析圖表 (PNG)，便於財務報告引用。

## 執行產出
執行專案後，系統會自動在根目錄產出：
- `output/dupont_analysis.png`: 包含三階段指標的視覺化柱狀圖。

## 如何使用

請依照以下步驟在您的本地環境中部署並執行此工具：

### 1. 複製本專案
打開終端機，執行以下指令將專案下載至本地：
```bash
git clone [https://github.com/Thomas-2032/Financial-DuPont-Analyzer.git](https://github.com/Thomas-2032/Financial-DuPont-Analyzer.git)
cd Financial-DuPont-Analyzer

# 建立虛擬環境
python -m venv venv

# 啟動虛擬環境 (Windows)
venv\Scripts\activate
# 啟動虛擬環境 (Mac/Linux)
source venv/bin/activate

pip install -r requirements.txt

python src/main.py