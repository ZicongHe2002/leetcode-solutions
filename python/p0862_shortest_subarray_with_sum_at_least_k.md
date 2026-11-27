# 862. Shortest Subarray with Sum at Least K · Python

[原题](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/)。

允许负数，普通正数滑动窗口不适用。队列保存下标递增且前缀和严格递增的候选起点。当前前缀与队首差达到k时记录区间，再弹队首；同一起点以后只会形成更长区间，已无保留必要。新前缀不大于队尾时，新下标更晚、前缀更小，对任何未来终点都不劣，因此删去队尾。初始(0,0)覆盖从首项开始的区间，无解返回-1。

每个前缀进出队列至多一次，时间O(n)，额外空间O(n)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
