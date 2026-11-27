# 915. Partition Array into Disjoint Intervals · Python

[原题](https://leetcode.com/problems/partition-array-into-disjoint-intervals/)。

初始左区只含首项，left_maximum是当前强制左区最大值，prefix_maximum是扫描至今所有值最大值。后面出现小于left_maximum的值时，它不能留在右区，任何合法边界都必须至少延伸到此处；扩区同时纳入此前所有中间值，更新left_maximum为整个已扫描前缀最大值。只在被迫时扩区，所以结束得到最短合法左区。等值允许留在右区，判断用严格小于，题目保证存在非空双区划分。

时间O(n)，额外空间O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
