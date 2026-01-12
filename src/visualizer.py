import matplotlib.pyplot as plt

def plot_dupont(results):
    """繪製杜邦分析組成的柱狀圖"""
    labels = ['Net Profit Margin', 'Asset Turnover', 'Equity Multiplier']
    values = [results['Net Profit Margin'], results['Asset Turnover'], results['Equity Multiplier']]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, color=['#4CAF50', '#2196F3', '#FF9800'])
    
    plt.title(f"DuPont Analysis - {results['Ticker']}", fontsize=14)
    plt.ylabel("Ratio Value")
    
    # 在柱狀圖上方顯示數值
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 4), va='bottom')
        
    plt.show()