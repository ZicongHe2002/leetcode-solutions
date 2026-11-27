# 1054. Distant Barcodes · Python

[原题](https://leetcode.com/problems/distant-barcodes/)。

最大频次堆选择最急需安排的值，但上一位刚用的值暂不在堆内，因此当前不可能与它相同。选择后把更早暂扣值的剩余次数放回，再暂扣当前值。题目保证存在无相邻重复排列，这个最多优先且只冷却一位的过程可消费全部频次，不改变元素多重集。只读原数组，返回任意合法新排列。

N项U种值，时间O(N log U)，空间O(N+U)包含输出。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
