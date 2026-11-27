# 916. Word Subsets · Python

[原题](https://leetcode.com/problems/word-subsets/)。

候选必须分别包含words2每个词的全部字母频次，不要求同时消耗不同约束词，所以同一字母需求应取各词最大次数而非求和。Counter的并集操作正是逐键取最大值。合并后逐候选检查全部需求，保留原候选次序和重复项，不修改输入。

总字符数L、候选数W、小写字母表26，期望时间O(L+26W)，除输出外额外空间O(26)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
