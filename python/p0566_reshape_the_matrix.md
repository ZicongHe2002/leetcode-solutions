# 566. Reshape the Matrix · Python

[原题](https://leetcode.com/problems/reshape-the-matrix/)。

原题mat行列数分别1..100，元素在-1000..1000，目标r、c分别1..300。合法重塑必须保留总元素数，按原先逐行顺序填入目标矩阵；若数量不同就返回原矩阵。输入内容保持，返回list[list[int]]。

先检查rows*columns==r*c，不相等直接返回原对象。相等时行优先线性下标index在原矩阵对应(index//columns,index%columns)，在新矩阵对应(index//c,index%c)，逐项复制便保持整条行序不变。目标各行分别分配，成功时新结果不共享输入行；相同目标形状也可得到内容相等的新矩阵。合法重塑时间O(rows*columns)，输出空间O(rows*columns)、除输出外额外空间O(1)；不合法请求时间和额外空间O(1)。

独立参考先逐行拉平，再用长度c的连续切片分块，不使用两边商余映射。1..3行列全部682个二值矩阵，分别尝试r、c为1..4，共10912次请求，核对成功形状、原对象返回和输入保持；另测100行列上界、300行或300列的合法目标、值域端点和矩形互换。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
