# 838. Push Dominoes · Python

[原题](https://leetcode.com/problems/push-dominoes/)。

左到右传播R的影响，遇到R重置强度为串长，遇到L阻断，空位每走一格减1。右到左对L做同样传播并从净作用中减去。初始强度只用于表示距离，距离更近的来源强度更大；两侧同时到达时强度抵消，牌保持竖直，无影响也竖直。原有R或L阻断相反方向传播，保留其初始方向。

时间O(n)，额外空间O(n)，不做逐时刻全串模拟，输入字符串保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
