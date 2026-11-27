# 1130. Minimum Cost Tree From Leaf Values · Python

[原题](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/)。

叶子顺序固定，内部节点代价为左右子树最大叶值的乘积。局部较小叶值迟早需要与相邻某侧更大叶值合并，应先与两侧可选较大值中较小者合并，这样消去该叶值后不会改变剩余区间最大值。递减栈保留尚未消去的叶值，当前值使栈顶出栈时，两侧候选正是新栈顶与当前值。末尾残留递减链按相邻值依次合并。

每项入栈出栈一次，时间O(n)，额外空间O(n)，不修改输入。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
