# 988. Smallest String Starting From Leaf · Python

[原题](https://leetcode.com/problems/smallest-string-starting-from-leaf/)。

节点值0..25映射a..z。显式DFS进入节点时把字符压入根路径，退出事件弹出，确保兄弟分支不混入彼此路径。只有真实叶子能作起点，将当前根到叶路径反向连接成叶到根候选，再作字典序比较。不能只选最浅叶或直接比较根到叶字符串，前缀相同时较短字符串自然更小。

N节点、L叶、最大高度H，时间O(N+LH)，共享路径与事件栈及最优串空间O(H)。不依赖深链递归，不修改原树。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
