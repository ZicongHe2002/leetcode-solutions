# 1200. Minimum Absolute Difference · Python

[原题](https://leetcode.com/problems/minimum-absolute-difference/)。

输入至少两个互异整数。非相邻两数之间存在中间数，其差一定大于某个相邻差，因此最小绝对差只需考察排序后的相邻项。遇到更小差时清空旧答案，遇到相等差时追加；扫描顺序自然满足每对递增及答案数对升序。

时间O(n log n)，排序和输出空间O(n)，不修改原数组。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
