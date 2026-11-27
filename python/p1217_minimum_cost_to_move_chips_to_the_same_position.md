# 1217. Minimum Cost to Move Chips to The Same Position · Python

[原题](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/)。

移动两格费用0，移动一格费用1，因此所有偶数位置芯片可免费汇合，所有奇数位置芯片也可免费汇合。最终选偶数目标时每个奇数组芯片至少花1，选奇数目标时反之，取两组人数较小者。相同坐标的多个芯片仍分别计费，具体坐标距离不影响最小费用。

时间O(n)，额外空间O(1)，不修改芯片位置。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
