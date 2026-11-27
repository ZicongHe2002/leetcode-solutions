# 940. Distinct Subsequences II · Python

[原题](https://leetcode.com/problems/distinct-subsequences-ii/)。

total计入空子序列。新字符到来，每个旧子序列可不加或加它，先得到2*total；若该字符之前出现过，旧前缀在上次该字符前的每个子序列追加它，已形成过相同末字符序列，需要减去当时的total。保存本轮变更前total为该字符下次去重基数，最后减去空序列并按10^9+7取模。

时间O(n)，字母表额外空间O(26)，不枚举所有子序列文本，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
