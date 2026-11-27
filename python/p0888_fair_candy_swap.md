# 888. Fair Candy Swap · Python

[原题](https://leetcode.com/problems/fair-candy-swap/)。

设双方总量A、B，交换Alice的a与Bob的b后平衡要求A-a+b=B-b+a，故a-b=(A-B)/2。题目保证存在解，因此总差为偶数。把Bob所有盒子大小存集合，逐个Alice值查找a-差值即可，返回的顺序为Alice值、Bob值。重复大小不影响是否存在盒子，输入保持。

两数组长度N和M，期望时间O(N+M)，额外空间O(M)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
