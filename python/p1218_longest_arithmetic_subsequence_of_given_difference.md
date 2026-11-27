# 1218. Longest Arithmetic Subsequence of Given Difference · Python

[原题](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/)。

子序列需要保持原有下标顺序，但元素不必连续。当前值value只能接在value-difference之后，因此扫描到它时，字典中该前驱值的最优长度加1就是新候选。更新前先读取旧状态，difference=0时也只是把此前同值序列延长一次，不会复用当前元素。字典只存各结尾值的最大长度，负公差、零公差和重复值统一处理。

期望时间O(n)，额外空间O(D)，D为不同值数，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
