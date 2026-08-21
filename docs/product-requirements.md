# Product Requirements: v0.1 Core Engine

## 1. Goal

使用者輸入股票代號後，系統取得可用的年度財務報表，
並使用三階段 DuPont 模型分析企業 ROE 的來源。

## 2. User Story

身為使用者，我希望輸入股票代號與分析年度數量，
查看企業的淨利率、資產週轉率、權益乘數與 ROE，
以便了解 ROE 主要來自獲利能力、資產效率或財務槓桿。

## 3. In Scope

v0.1 包含：

- 支援年度財務報表
- 接受 Yahoo Finance 股票代號
- 支援使用者指定分析年度數量
- 使用三階段 DuPont 模型
- 使用平均總資產與平均股東權益
- 顯示財務期間與資料來源
- 顯示資料不足或特殊財務狀況的警告
- 提供 CLI 操作介面
- 提供自動化測試

## 4. Out of Scope

v0.1 不包含：

- 季度財務報表
- FastAPI
- Next.js 前端
- 使用者登入
- 資料庫
- PDF 報告
- 即時股價
- 投資建議
- SEC EDGAR 與 TWSE OpenAPI

## 5. Input Requirements

### Ticker

- 股票代號不得為空
- 系統應將股票代號轉換成大寫
- 股票代號必須能由資料來源辨識

範例：

```text
AAPL
MSFT
2330.TW
```

### Years

- 必須是整數
- 必須大於或等於 1
- 系統最多回傳使用者指定的年度數量
- 若資料不足，回傳所有可計算年度並附加警告

## 6. Required Financial Data

每個可計算年度需要：

- Net Income
- Total Revenue
- Beginning Total Assets
- Ending Total Assets
- Beginning Stockholders Equity
- Ending Stockholders Equity
- Financial Period End Date

計算一個年度需要兩期資產負債表資料。

## 7. DuPont Formula

平均總資產：

```text
Average Assets =
(Beginning Total Assets + Ending Total Assets) / 2
```

平均股東權益：

```text
Average Equity =
(Beginning Stockholders Equity + Ending Stockholders Equity) / 2
```

淨利率：

```text
Net Profit Margin =
Net Income / Total Revenue
```

資產週轉率：

```text
Asset Turnover =
Total Revenue / Average Assets
```

權益乘數：

```text
Equity Multiplier =
Average Assets / Average Equity
```

股東權益報酬率：

```text
ROE =
Net Profit Margin × Asset Turnover × Equity Multiplier
```

## 8. Output Requirements

每個年度的分析結果應包含：

- Ticker
- Financial Period End Date
- Average Assets
- Average Equity
- Net Profit Margin
- Asset Turnover
- Equity Multiplier
- ROE
- Data Source
- Warnings

結果應依財務期間由新到舊排列。

## 9. Error and Warning Rules

- 營收為零：拒絕計算該年度
- 平均資產為零：拒絕計算該年度
- 平均權益為零：拒絕計算該年度
- 平均權益為負：允許計算，但加入 NEGATIVE_EQUITY 警告
- 缺少期初資料：該年度無法計算
- 缺少必要財務欄位：回傳結構化錯誤
- 股票代號不存在：回傳明確錯誤
- 外部資料來源失敗：回傳 Provider Error
- 可計算年度少於要求：回傳現有資料並加入警告
- v0.1 不提供金融業專用 DuPont 模型，金融業結果必須顯示適用性警告

## 10. Data Source and Disclaimer

v0.1 使用 yfinance 取得 Yahoo Finance 公開資料。

yfinance 並非 Yahoo 官方、背書或審核的產品，資料主要供研究與教育用途。系統必須顯示：

```text
This project is for educational and demonstration purposes only.
The results do not constitute investment advice.
```

## 11. Acceptance Criteria

- 使用者可以輸入股票代號
- 使用者可以指定年度數量
- 系統使用年度財務報表
- 系統使用平均總資產
- 系統使用平均股東權益
- 系統正確計算三項 DuPont 指標
- ROE 等於三項指標乘積
- 結果依財務期間由新到舊排列
- 資料缺失時提供明確錯誤或警告
- 計算核心不直接依賴 yfinance
- 自動化測試不依賴網路
- CLI 可以執行分析
- 顯示資料來源與非投資建議聲明
