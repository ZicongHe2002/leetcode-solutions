# 882. Reachable Nodes In Subdivided Graph · Python

[原题](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/)。

原边含c个新增节点，穿越它到另一原端点需要c+1步。在原节点构成的加权图上从0做Dijkstra，只保留预算内的原节点最短距离。每条边可从两端各走max(0,maxMoves-distance)步，覆盖其中这么多新增节点；两侧可能相遇，取两侧数量和与c的较小值，避免重复。每条细分边独立计新增节点，原节点另外计一次。

设原节点N、边E，时间O((N+E)log(N+E))，空间O(N+E)。不显式展开大量细分节点，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
