# 952. Largest Component Size by Common Factor · Python

[原题](https://leetcode.com/problems/largest-component-size-by-common-factor/)。

两值公因子大于1当且仅当共享某个质因子。分解每个数，按不同质因子记录一个已见下标，把后续含该因子的数与之合并；质因子重复幂只处理一次。剩余大于1的因子必为质数，也要归并。值1没有质因子，保留独立分量。最后按下标根计数取最大，所有连接的传递性由并查集处理。

N个数、最大值M、出现过F个质因子，试除实现时间上界O(N sqrt(M) alpha(N))，额外空间O(N+F)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
