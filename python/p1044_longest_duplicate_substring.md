# 1044. Longest Duplicate Substring · Python

[原题](https://leetcode.com/problems/longest-duplicate-substring/)。

倍增排序后缀，排名键为当前位置前width段排名与下一段排名，越界用-1。每轮重新编号相等键并将width翻倍，直到所有后缀有唯一排名。重复子串是某两个后缀公共前缀，排序后最长值必可在相邻后缀间找到；Kasai利用前一位置LCP减1作为起点，线性累计相邻LCP。返回最长对应原串切片，允许两次出现重叠，无重复返回空串。

Python比较排序的倍增时间O(n log^2 n)，LCP扫描O(n)，额外空间O(n)。没有复制全部后缀文本，也不依赖滚动哈希碰撞假设。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
