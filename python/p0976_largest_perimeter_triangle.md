# 976. Largest Perimeter Triangle · Python

[原题](https://leetcode.com/problems/largest-perimeter-triangle/)。

正边长排序后只需检查较小两边之和严格大于最大边。若当前最大边与紧邻的两条较大前边仍不能构成三角形，换任何更小边也不行，可丢弃该最大边。首次满足的连续三边是剩余所有值中最大的三项，其周长也不小于之后更小最大边的任何候选。无合法三角形返回0，相等时是退化三角形，不能接受。

时间O(n log n)，排序副本空间O(n)，输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
