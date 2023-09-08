import argparse
import numpy as np

# 解析命令行参数
parser = argparse.ArgumentParser(description='Count data points in a 2D grid and save results')
parser.add_argument('-x', type=float, help='Length of the x-axis')
parser.add_argument('-y', type=float, help='Length of the y-axis')
parser.add_argument('-s', type=int, help='Number of grid cells')
parser.add_argument('-i', type=str, help='Input file with three columns: x, y, ID')
parser.add_argument('-o', type=str, help='Output file to save results')
args = parser.parse_args()

# 读取输入文件，假设文件中包含三列数据：x坐标、y坐标、ID
data = np.loadtxt(args.i, delimiter='\t', dtype={'names': ('x', 'y', 'ID'), 'formats': ('f4', 'f4', 'S10')})

# 根据格子数量计算网格边界
x_bins = np.linspace(0, args.x, args.s + 1)
y_bins = np.linspace(0, args.y, args.s + 1)

# 过滤掉超出范围的数据点
filtered_data = data[(data['x'] >= 0) & (data['x'] <= args.x) & (data['y'] >= 0) & (data['y'] <= args.y)]

# 使用np.histogram2d函数统计数据点落入格子的个数
hist, x_edges, y_edges = np.histogram2d(filtered_data['x'], filtered_data['y'], bins=(x_bins, y_bins))

# 获取每个格子中的ID
grid_ids = [[] for _ in range(args.s * args.s)]
for i in range(len(filtered_data)):
    x_idx = np.digitize(filtered_data['x'][i], x_edges) - 1
    y_idx = np.digitize(filtered_data['y'][i], y_edges) - 1
    grid_ids[y_idx * args.s + x_idx].append(filtered_data['ID'][i].decode('utf-8'))

# 将结果保存到输出文件中
with open(args.o, 'w') as output_file:
    output_file.write("Grid Position, Count, IDs\n")
    for i in range(len(x_bins) - 1):
        for j in range(len(y_bins) - 1):
            grid_position = f"({x_bins[i]:.2f}, {y_bins[j]:.2f})"
            count = int(hist[i, j])
            ids = ', '.join(grid_ids[j * args.s + i])
            output_file.write(f"{grid_position}, {count}, {ids}\n")

print(f"Results saved to {args.o}")

