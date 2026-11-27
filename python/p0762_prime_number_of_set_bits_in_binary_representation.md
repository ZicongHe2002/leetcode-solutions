# 762. Prime Number of Set Bits in Binary Representation · Python

[原题](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/)。

原题1<=left<=right<=10^6，right-left<=10^4。统计闭区间内二进制1的个数为质数的整数。这里检查的是置位数是否为质数，不是整数本身是否为质数；1不是质数。

10^6<2^20，因此原题整数最多20个二进制位，可能用到的置位质数恰在集合{2,3,5,7,11,13,17,19}中。对闭区间每个整数调用bit_count，再检查集合成员并累加布尔值；range的上端加1确保包含right。固定上界下每次置位计数处理有界整数，设W=right-left+1，总时间O(W)，额外空间O(1)。若推广为任意大整数，则必须重新处理质数集合及置位运算成本，不能直接沿用本题固定集合。

独立oracle把整数格式化为二进制文本并数1，再逐个尝试2..count-1的除数判质数，不复用bit_count或固定质数表。1..127全部8128个非空闭区间均核对；另核对100个固定种子合法大范围区间、10^6端点、宽度10000、2的幂置位数1应不计入、19个1应计入和官方例。未向LeetCode提交。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
