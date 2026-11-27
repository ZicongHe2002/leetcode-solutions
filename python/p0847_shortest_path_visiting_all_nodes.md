# 847. Shortest Path Visiting All Nodes · Python

[原题](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)。

允许任意起点并可重复走节点，状态必须同时包含当前位置和已访问集合；同一个节点在不同集合下不能合并。用位掩码表示集合，把每个单节点起点以距离0同时入队。每条图边产生一步，BFS第一次到达全访问掩码即是任意起点中的最短距离。重复状态只保留首次，单节点图不必走边。

N个节点E条边，时间O((N+E)*2^N)，额外空间O(N*2^N)。输入图保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
