# 849. Maximize Distance to Closest Person · Python

[原题](https://leetcode.com/problems/maximize-distance-to-closest-person/)。

题目保证至少一个空座且至少一个已坐人。最前已坐人之前的空段，选首位可获得距离等于该已坐人下标；最后已坐人后的空段选末位。两个已坐人下标p和q之间，最优位置靠中间，最近距离为floor((q-p)/2)。扫描每个占用位置更新这三类候选，不需要为每个空座搜索两边。

时间O(n)，额外空间O(1)，输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
