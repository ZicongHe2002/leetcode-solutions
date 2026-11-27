# 1034. Coloring A Border · Python

[原题](https://leetcode.com/problems/coloring-a-border/)。

只遍历与给定起点四邻连通且同原色的分量。分量格若有任一邻边越出网格或接到异色格，就是该分量边界；四邻都在分量内则保留原色。搜索始终读取未改动原图，避免先染色导致后续错误判断同色关系。最后在副本一次改全部边界，分量外格和内部格不变。

时间O(RC)，已见集合、栈和结果副本总空间O(RC)，原网格保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
