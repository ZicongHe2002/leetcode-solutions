# 1171. Remove Zero Sum Consecutive Nodes from Linked List · Python

[原题](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/)。

若两个节点处的累计和相同，它们之间的连续节点和为0。第一遍记录每个前缀和最后出现的节点；第二遍把当前节点next直接指向最远相同前缀节点的后继，因此跳过完整零和段，也自动覆盖嵌套或相邻零和区间。跳过区间总和为0，后续保留节点的前缀和不变，可继续使用第一遍记录。哨兵处理从链表头开始删除的情况。

期望时间O(n)，额外空间O(n)，原地修改next链接，ListNode由LeetCode提供。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
