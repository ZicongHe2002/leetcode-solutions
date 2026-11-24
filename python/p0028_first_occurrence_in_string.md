# 28. Find the Index of the First Occurrence in a String · Python

[原题](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)。

原题haystack与needle长度均为1..10000，只含小写英文字母，返回needle首次出现的起始下标，没有匹配返回-1。本实现额外支持空haystack及空needle，空needle返回0；不会修改字符串。

先为needle构建borders：每项是该前缀的最长真前缀且同时为后缀的长度。失配时把matched回退到borders[matched-1]，保留已知相等的边界；直到可继续匹配或回到0，不把文本指针退回。扫描文本时用同样规则维护已匹配的模式前缀，首次达到完整长度就返回起点，因文本下标单调所以一定是首个匹配。每次成功最多让matched增1，回退总数也受增量限制，时间O(n+m)，额外空间O(m)。

独立oracle使用Python字符串find，核对二字母haystack长度0..5与needle长度0..4的全部1953对；空输入属于扩展。边界覆盖10000字符重复前缀、长模式、模式更长、复杂重叠边界及完全相等，检查下标int，不以某个非首次匹配充当答案。

A使用OpenAI Codex辅助编写；实际验证见PR与日志，未向LeetCode提交。完整初稿可由B正式review后按最终head普通merge，共同补写为可选，仅按真实内容署名。
