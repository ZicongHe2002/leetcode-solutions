# 935. Knight Dialer · Python

[原题](https://leetcode.com/problems/knight-dialer/)。

长度1时每个数字键各形成一种号码，包括无法继续跳的5。之后末键digit的计数等于所有可一步跳到它的旧末键计数之和。骑士关系无向，固定邻接表同时可用于反向求和。每轮另建10项数组，不把本轮新计数混入旧状态，最终求所有末键总和并模10^9+7。

时间O(n)，固定10状态额外空间O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
