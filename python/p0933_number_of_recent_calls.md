# 933. Number of Recent Calls · Python

[原题](https://leetcode.com/problems/number-of-recent-calls/)。

时间戳严格递增，新请求压到队尾。只有小于t-3000的旧项过期，恰好等于下界的请求仍在闭区间内，所以判断用<。队首是最早项，持续弹出过期项后，队列全部元素恰是本次查询的最近请求，新请求自身确保队列非空。

每次请求进出队列至多一次，ping摊还O(1)，空间为当前窗口请求数。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
