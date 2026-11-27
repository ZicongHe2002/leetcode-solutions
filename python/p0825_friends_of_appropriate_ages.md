# 825. Friends Of Appropriate Ages · Python

[原题](https://leetcode.com/problems/friends-of-appropriate-ages/)。

发送者年龄a的合法接收者年龄b必须满足b>0.5a+7且b<=a；题目另一个b>100且a<100的禁用条件已被b<=a包含。a<15时不存在合法年龄。a>=15时，以频次前缀和求闭区间[floor(a/2)+8,a]的人数，然后减去发送者本人，乘以该年龄的发送者人数。相同年龄的不同人可以互发，必须按有向请求计数。

年龄上限120固定，时间O(n+120)，额外空间O(120)，不修改输入。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
