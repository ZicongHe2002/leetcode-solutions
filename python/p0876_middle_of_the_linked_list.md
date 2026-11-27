# 876. Middle of the Linked List · Python

[原题](https://leetcode.com/problems/middle-of-the-linked-list/)。

快慢指针同起于头，每轮快走两条边、慢走一条边。快指针到尾或越过尾时，慢指针正好到中间；偶数长度时快指针越过尾，慢指针落在两个中点的第二个，符合题目要求。返回实际ListNode而不是值或复制链表，不修改链接。

时间O(n)，额外空间O(1)。LeetCode提供ListNode。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
