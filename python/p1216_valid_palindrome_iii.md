# 1216. Valid Palindrome III · Python

[原题](https://leetcode.com/problems/valid-palindrome-iii/)。

输入非空，目标是删除至多k个字符后形成回文。区间两端相同可同时保留，代价等于内部区间；不同时至少删除一端，取两个子问题较小值加1。left倒序、right正序更新，一维deletions[right]更新前为下一行状态，deletions[right-1]为本行左侧状态，diagonal保留上一行左上角值。单字符或空内部区间代价0，最终比较全串最少删除数是否不超过k。

时间O(n^2)，额外空间O(n)，不构造所有删除方案。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
