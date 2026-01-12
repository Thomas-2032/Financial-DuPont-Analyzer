import yfinance as yf

class DuPontAnalyzer:
    def __init__(self, ticker_symbol):
        self.ticker_symbol = ticker_symbol
        self.stock = yf.Ticker(ticker_symbol)
        self.financials = None
        self.balance_sheet = None

    def fetch_data(self):
        """獲取利潤表與資產負債表數據"""
        try:
            print(f"正在從 Yahoo Finance 獲取 {self.ticker_symbol} 的數據...")
            self.financials = self.stock.financials
            self.balance_sheet = self.stock.balance_sheet
            if self.financials.empty or self.balance_sheet.empty:
                raise ValueError("抓取不到財報數據，請檢查代碼是否正確。")
        except Exception as e:
            print(f"錯誤：{e}")

    def calculate_dupont(self):
        """實作杜邦分析邏輯"""
        net_income = self.financials.loc['Net Income'].iloc[0]
        revenue = self.financials.loc['Total Revenue'].iloc[0]
        total_assets = self.balance_sheet.loc['Total Assets'].iloc[0]
        total_equity = self.balance_sheet.loc['Stockholders Equity'].iloc[0]

        # 杜邦三率
        net_profit_margin = net_income / revenue
        asset_turnover = revenue / total_assets
        equity_multiplier = total_assets / total_equity
        roe = net_profit_margin * asset_turnover * equity_multiplier

        return {
            "Ticker": self.ticker_symbol,
            "Net Profit Margin": net_profit_margin,
            "Asset Turnover": asset_turnover,
            "Equity Multiplier": equity_multiplier,
            "ROE": roe
        }