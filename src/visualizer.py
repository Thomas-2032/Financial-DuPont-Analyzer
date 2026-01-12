import matplotlib.pyplot as plt
import os  # 引入作業系統模組

def plot_dupont(results, filename="dupont_analysis.png"):
    """繪製杜邦分析圖並儲存至 output 資料夾"""
    
    # 1. 確保 output 資料夾存在
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"已建立目錄: {output_dir}")

    # 2. 繪圖邏輯
    labels = ['Net Profit Margin', 'Asset Turnover', 'Equity Multiplier']
    values = [results['Net Profit Margin'], results['Asset Turnover'], results['Equity Multiplier']]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, color=['#4CAF50', '#2196F3', '#FF9800'])
    plt.title(f"DuPont Analysis - {results['Ticker']}", fontsize=14)
    plt.ylabel("Ratio Value")
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 4), va='bottom')

    # 3. 關鍵修正：將路徑指向 output 資料夾
    save_path = os.path.join(output_dir, filename)
    plt.savefig(save_path, dpi=300) 
    print(f"圖表已成功儲存至: {save_path}")
    
    plt.show()