# 819. Most Common Word · Python

[原题](https://leetcode.com/problems/most-common-word/)。

词不区分大小写，先统一小写，再按连续英文字母提取词，把标点当分隔。只统计不在禁用集合中的词。题目保证至少一个非禁用词且最高频答案唯一，因此直接按计数取最大键，不额外创造平局规则。输入不修改。

设段落总字符数P、禁用词总字符数B，期望时间O(P+B)，额外空间O(P+B)，包含分词列表和计数表。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
