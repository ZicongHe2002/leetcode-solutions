# 1167. Minimum Cost to Connect Sticks · Python

[原题](https://leetcode.com/problems/minimum-cost-to-connect-sticks/)。

合并两根木棍的代价和新长度都等于两者之和。合并过程可表示为二叉树，每根原木棍对总代价的贡献等于长度乘以其合并深度。最小的两个长度可放在最深的兄弟叶子位置而不增代价，因此先合并它们是安全选择，缩成一根后递归得到同类子问题。最小堆高效重复取两根最短项，只有一根时费用0。

时间O(n log n)，额外空间O(n)，堆使用副本，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
