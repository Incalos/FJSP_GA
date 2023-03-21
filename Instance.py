# Processing_time：工件各工序对应各机器加工时间矩阵
# J：各工件对应的工序数字典
# M_num：加工机器数
# O_num：加工工序数
# J_num：工件个数


CKS201 = [[10, 9, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
          [9999, 9999, 14, 16, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
          [9999, 9999, 9999, 9999, 15, 25, 21, 9999, 9999, 9999, 9999, 9999],
          [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9, 13, 15, 24, 9999],
          [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 10]]
CKS301 = [[12, 9, 10, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
          [9999, 9999, 9999, 16, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
          [9999, 9999, 9999, 9999, 15, 9999, 9999, 9999, 9999, 9999, 9999, 9999],
          [9999, 9999, 9999, 9999, 9999, 27, 22, 9999, 9999, 9999, 9999, 9999],
          [9999, 9999, 9999, 9999, 9999, 9999, 9999, 21, 17, 9999, 9999, 9999],
          [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 19, 9999, 9999],
          [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 17, 9999],
          [9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 9999, 18]]
Processing_time = [CKS201] * 3
Processing_time.extend([CKS301] * 4)
J = {i: 5 for i in range(1, 4)}
J.update({j: 8 for j in range(4, 8)})
M_num = 12
O_num = 3 * 5 + 4 * 8
J_num = 7
