import pandas as pd
import matplotlib.pyplot as plt

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
    import matplotlib.pyplot as plt

# 创建一个柱状图来显示不同年龄段的 'EmoQ5' 平均值
age_groups = data.groupby('age')['EmoQ5'].mean()

plt.figure(figsize=(10, 6))
age_groups.plot(kind='bar', color='skyblue')
plt.title('不同年龄段的EmoQ5平均值')
plt.xlabel('年龄段')
plt.ylabel('EmoQ5平均值')
plt.xticks(rotation=45)
plt.show()


