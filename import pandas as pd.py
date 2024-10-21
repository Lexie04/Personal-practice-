import pandas as pd

file_path = '/Users/liyifan/Desktop/数据分析/论文数据分析最终结果/boot2.xlsx'  
sheet_name = 'boot1'  # 工作表名称
data = pd.read_excel(file_path, sheet_name=sheet_name)
if 'EmoQ5' in data.columns:
    filtered_data = data[data['EmoQ5'] == 5]
    print(filtered_data)
    output_path = '/Users/liyifan/Desktop/filtered_emoq5.xlsx'  
    filtered_data.to_excel(output_path, index=False)
    print(f"筛选结果已保存到: {output_path}")
else:
    print("错误：未找到名为 'EmoQ5' 的列，请检查你的Excel文件格式。")

