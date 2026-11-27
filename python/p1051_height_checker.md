# 1051. Height Checker · Python

[原题](https://leetcode.com/problems/height-checker/)。

题目统计的是当前站位与应有非递减身高序列不一致的位置数，不是最少交换次数。排序副本给唯一的目标值序列，逐位置比较即可，重复身高以值匹配，不要求区分同高学生身份。原heights保持不变。

时间O(n log n)，排序副本空间O(n)，比较额外空间O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
