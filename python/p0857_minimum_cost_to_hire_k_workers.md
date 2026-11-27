# 857. Minimum Cost to Hire K Workers · Python

[原题](https://leetcode.com/problems/minimum-cost-to-hire-k-workers/)。

同组工资必须与质量成正比，统一比例至少是组内各人最低工资/质量的最大值。按该比值递增扫描，当前比值作为候选统一比例；已扫描工人都接受该比例，选其中k个最小质量使总成本最小。负数最大堆超过k人就移除最大质量，维护质量和。对所有候选比例取最低成本，覆盖最优组的最大比值所在位置。

Fraction使比例排序和成本比较保持有理数精确，最后转float返回。按题目有界整数算术计，时间O(n log n+n log k)，额外空间O(n+k)，输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
