# 979. Distribute Coins in Binary Tree · Python

[原题](https://leetcode.com/problems/distribute-coins-in-binary-tree/)。

子树若金币数比节点数多b，必须经唯一父边净流出b枚，缺少则净流入-b枚，边上至少要abs(b)次移动。后序把左右净余量交给当前节点，加本节点金币再减去自身应留1枚，得到向父亲的净余量；两条子边各累计其绝对流量。各边净流量不可避免，也能由后序实际搬运实现，故总和最小。题目总金币等于总节点，根最终无需向树外搬运。

时间O(n)，显式后序与状态表额外空间O(n)，不修改节点金币或链接，TreeNode由LeetCode提供。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
