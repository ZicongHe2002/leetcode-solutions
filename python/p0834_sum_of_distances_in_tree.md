# 834. Sum of Distances in Tree · Python

[原题](https://leetcode.com/problems/sum-of-distances-in-tree/)。

先以0为根迭代遍历，记录父节点、深度与父先于子的顺序，深度和就是根0到全部点的距离和。逆序把各子树大小加给父节点。再正序把根从父节点移到孩子：孩子子树中的subtree个节点距离都减1，其他n-subtree个节点都加1，因此答案变化为n-2*subtree。每个节点都由已知父答案得到一次。

输入保证为树，跳过父边即可，无需一般图环检测。时间O(n)，额外空间O(n)，迭代顺序避免长链递归栈，edges保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
