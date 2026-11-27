# 1160. Find Words That Can Be Formed by Characters · Python

[原题](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/)。

每个单词独立使用chars，不能在处理前一个单词后永久消耗字符。一个词可构造当且仅当它每种字母需求都不超过可用频次，单纯检查字母集合会漏掉重复需求。所有合格单词按各自长度累计，相同文本若在输入出现多次，也分别计入。

时间O(len(chars)+所有词总长度)，小写字母表固定，除输入外额外空间O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
