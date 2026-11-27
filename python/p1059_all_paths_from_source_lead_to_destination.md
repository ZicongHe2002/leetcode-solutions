# 1059. All Paths from Source Lead to Destination · Python

[原题](https://leetcode.com/problems/all-paths-from-source-lead-to-destination/)。

所有可达路径必须有限且最终停在destination，所以目标本身不能有出边，其他可达无出边节点也不允许。三色DFS中1表示当前路径上，遇1即存在可无限绕行的环；2表示该点全部后继已通过，可复用结论。显式栈保存下一条待处理出边，只有所有后继完成才标2，不能把仅已发现的节点当作安全。不相关不可达环不影响答案。

时间O(n+E)，邻接表、颜色与显式栈空间O(n+E)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
