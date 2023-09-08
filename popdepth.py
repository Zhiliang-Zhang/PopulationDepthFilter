import argparse
import numpy as np

# 解析命令行参数
parser = argparse.ArgumentParser(description='Count data points in a 2D grid and save results')
parser.add_argument('-x', type=float, help='Length of the x-axis')
parser.add_argument('-y', type=float, help='Length of the y-axis')
parser.add_argument('-s', type=int, help='Number of grid cells')
parser.add_argument('-i', type=str, help='Input file with two columns of decimal data')
parser.add_argument('-o', type=str, help='Output file to save results')
args = parser.parse_args()

# 读取输入文件，假设文件中包含两列小数数据，分别代表 x 和 y 坐标
data = np.loadtxt(args.i, delimiter='\t')  # 使用制表符作为分隔符

# 过滤超出指定范围的数据点
filtered_data = data[(data[:, 0] >= 0) & (data[:, 0] <= args.x) & (data[:, 1] >= 0) & (data[:, 1] <= args.y)]

# 根据格子数量计算网格边界
x_bins = np.linspace(0, args.x, args.s + 1)
y_bins = np.linspace(0, args.y, args.s + 1)

# 使用np.histogram2d函数统计筛选后的数据点落入格子的个数
hist, x_edges, y_edges = np.histogram2d(filtered_data[:, 0], filtered_data[:, 1], bins=(x_bins, y_bins))

# 将结果保存到输出文件中
with open(args.o, 'w') as output_file:
    output_file.write("Grid Position, Count\n")
    for i in range(len(x_bins) - 1):
        for j in range(len(y_bins) - 1):
            grid_position = f"({x_bins[i]:.2f}, {y_bins[j]:.2f})"
            count = int(hist[i, j])
            output_file.write(f"{grid_position}, {count}\n")

print(f"Results saved to {args.o}")

