# 839. Similar String Groups · Python

[原题](https://leetcode.com/problems/similar-string-groups/)。

题目字符串等长且互为字母重排。两个词相同，或恰有两处不同且这两处字符交叉对应时，可通过至多一次交换变为彼此。超过两处不同立即排除。将相似关系视为无向边，题目要求的是边的传递连通分量，而不是组内任意两词都直接相似，因此逐对判断后用并查集合并。每次真正合并减少组数，重复词也能归为同组。

词数W、词长L，时间O(W^2*(L+alpha(W)))，额外空间O(W)，不修改输入。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
