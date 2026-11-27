# 1019. Next Greater Node In Linked List · Python

[原题](https://leetcode.com/problems/next-greater-node-in-linked-list/)。

从头向后遍历，栈中旧节点值保持非递增。新节点比栈顶大时，它就是该旧节点右侧首个严格更大值，弹出并写答案，直到栈顶不再更小。相等不能结算，必须继续等待严格更大值。每个节点先默认答案0，结束仍在栈中的节点没有更大后继。只读ListNode，不修改链表。

每项进出栈一次，时间O(n)，输出和等待栈空间O(n)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
