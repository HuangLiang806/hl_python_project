# coding = utf-8
import numpy as np

__author__ = 'huangliang'
__version__ = 'v1.0'


# 图像化输出给定的矩阵
def print_number(a):
    for i in range(30):
        if i % 5 == 0:
            print('')
        if a[i] == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')
    return None


def my_neural_net(p):
    # a = hardlims(wp)
    # return: list
    a0_hl = [-1, 1, 1, 1, -1,
             1, -1, -1, -1, 1,
             1, -1, -1, -1, 1,
             1, -1, -1, -1, 1,
             1, -1, -1, -1, 1,
             -1, 1, 1, 1, -1]
    a1_hl = [-1, 1, 1, -1, -1,
             -1, -1, 1, -1, -1,
             -1, -1, 1, -1, -1,
             -1, -1, 1, -1, -1,
             -1, -1, 1, -1, -1,
             -1, -1, 1, -1, -1]
    a2_hl = [1, 1, 1, -1, -1,
             -1, -1, -1, 1, -1,
             -1, -1, -1, 1, -1,
             -1, 1, 1, -1, -1,
             -1, 1, -1, -1, -1,
             -1, 1, 1, 1, 1]
    # # 输出阵列
    # for i in range(3):
    #     print('打印数字%d的矩阵:' % (i))
    #     print_number(eval('a'+str(i)))

    # 转换为矩阵
    m0 = np.mat(a0_hl)
    m1 = np.mat(a1_hl)
    m2 = np.mat(a2_hl)
    p_matrix = np.mat(p)

    # 计算权值矩阵
    w = m0.T * m0 + m1.T * m1 + m2.T * m2

    n_matrix = w * p_matrix.T

    # 实现hardlims函数
    n_array = np.array(n_matrix)
    a = []
    for i in range(30):
        a.append(1 if n_array[i] >= 0 else 0)

    return a


def main():
    # 数据缺失，噪音数据 测试
    a0_hl_noise = [-1, -1, 1, 1, -1,
                   1, -1, -1, 1, -1,
                   1, -1, -1, -1, 1,
                   -1, -1, -1, -1, -1,
                   1, -1, 1, -1, 1,
                   -1, 1, -1, 1, -1]
    a0_hl_queshi = [-1, 1, 1, 1, -1,
                    1, -1, -1, -1, 1,
                    1, -1, -1, -1, 1,
                    -1, -1, -1, -1, -1,
                    -1, -1, -1, -1, -1,
                    -1, -1, -1, -1, -1]

    # 测试含有噪声数据的 0
    print('当前输入数据（含有噪声）为：')
    print_number(a0_hl_noise)
    a0_hl_noise_net_output = my_neural_net(a0_hl_noise)
    print(('神经网络输出数据为：'))
    print(a0_hl_noise_net_output)
    print_number(a0_hl_noise_net_output)

    print('-' * 86)
    # 测试含有缺失数据的 0
    print('当前输入数据(部分缺失）为：')
    print_number(a0_hl_queshi)
    a0_hl_queshi_net_output = my_neural_net(a0_hl_queshi)
    print(('神经网络输出数据为：'))
    print(a0_hl_queshi_net_output)
    print_number(a0_hl_queshi_net_output)


if __name__ == "__main__":
    main()
