# 826. Most Profit Assigning Work · Python

[原题](https://leetcode.com/problems/most-profit-assigning-work/)。

同一工作可分配给任意多个工人，因此工人之间没有消耗工作名额的竞争，每人独立选择能力可达的最高收益。把工作按难度排序、工人按能力排序，游标只向前扩展已可做工作，best保留这些工作的最高收益；没有可做工作时收益0。逐工人累加best即可。

工作数J、工人数W，时间O(J log J+W log W)，额外空间O(J+W)，排序均创建副本，输入不变。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
