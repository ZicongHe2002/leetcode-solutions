# 1092. Shortest Common Supersequence · Python

[原题](https://leetcode.com/problems/shortest-common-supersequence/)。

超序列必须分别保留两串作为子序列。能让两串共享的位置最多等于LCS长度，因此最短长度为n+m-LCS。用前缀动态规划求LCS后从右下角回溯：末字母相同就只放一次并同时消耗；不同时选能保留较大LCS长度的方向，放入该方向消耗的字母。一串耗尽后，另一串剩余字母全部补入。回溯按逆序生成，最后反转；平局任选一个最短答案即可。

时间O(nm+n+m)，额外空间O(nm+n+m)，两输入字符串保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
