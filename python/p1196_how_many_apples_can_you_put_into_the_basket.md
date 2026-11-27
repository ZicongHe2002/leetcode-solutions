# 1196. How Many Apples Can You Put into the Basket · Python

[原题](https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/)。

每颗苹果价值都为一颗，目标只最大化数量，重量为正且容量5000。若某方案选了较重苹果却没选更轻苹果，可交换而不增加总重，所以最优方案可取排序后的前缀。逐颗装入最轻项直到容量不足，后续更重项也不可能再加入。恰好5000仍合法。

时间O(n log n)，排序副本额外空间O(n)，原重量数组保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
