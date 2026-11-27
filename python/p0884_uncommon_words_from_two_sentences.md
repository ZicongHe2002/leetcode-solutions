# 884. Uncommon Words from Two Sentences · Python

[原题](https://leetcode.com/problems/uncommon-words-from-two-sentences/)。

要求某词在一句恰出现一次、另句完全不出现，等价于两句总频次恰为1。分别按空格分词后更新同一Counter，筛选计数1。仅做集合对称差会错误保留同句重复词，因此必须计数。题目允许任意输出顺序，输入保持。

总文本长度L，期望时间和额外空间O(L)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
