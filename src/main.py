from calculator import DuPontAnalyzer
from visualizer import plot_dupont

def run_analysis():
    # 以中信金 (2891.TW) 為例
    ticker = "2891.TW"
    
    analyzer = DuPontAnalyzer(ticker)
    analyzer.fetch_data()
    
    if analyzer.financials is not None:
        results = analyzer.calculate_dupont()
        
        print("\n=== 杜邦分析報告 ===")
        print(f"股票代號: {results['Ticker']}")
        print(f"1. 淨利率: {results['Net Profit Margin']:.4%}")
        print(f"2. 總資產週轉率: {results['Asset Turnover']:.4f}")
        print(f"3. 權益乘數: {results['Equity Multiplier']:.4f}")
        print("-" * 20)
        print(f"ROE (股東權益報酬率): {results['ROE']:.4%}")
        
        # 顯示圖表
        plot_dupont(results)

if __name__ == "__main__":
    run_analysis()