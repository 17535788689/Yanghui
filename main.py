
def generate_pascal_triangle(n):
    """生成杨辉三角的前n行"""
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

def print_pascal_triangle(triangle):
    """打印杨辉三角"""
    max_width = len(' '.join(map(str, triangle[-1])))
    for row in triangle:
        print(' '.join(map(str, row)).center(max_width))

if __name__ == '__main__':
    rows = int(input("请输入杨辉三角的行数: "))
    pascal_triangle = generate_pascal_triangle(rows)
    print_pascal_triangle(pascal_triangle)
