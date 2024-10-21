import pandas as pd


file_path = '/Users/liyifan/Desktop/申根签/法签文件/Trip liternary.xls'  
sheet_name = 'Sheet1'  
data = pd.read_excel(file_path, sheet_name=sheet_name)

print("数据中的缺失值概览：")
print(data.isnull().sum())


specific_value = '未来回去'  # 这里填写你想要的特定值，例如 '未知' 或 0
data_filled_specific = data.fillna(specific_value)

# 输出填充后的数据
print("\n用特定值填充后的数据：")
print(data_filled_specific)

# 保存填充后的数据到新的Excel文件
output_path = '/Users/liyifan/Desktop/filled_specific_value.xlsx'
data_filled_specific.to_excel(output_path, index=False)
print(f"\n填充后的数据已保存到: {output_path}")
