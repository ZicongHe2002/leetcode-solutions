# 516. Longest Palindromic Subsequence · Python

[原题](https://leetcode.com/problems/longest-palindromic-subsequence/)。

原题s长1..1000，只含小写英文，求保持原相对顺序的最长回文子序列长度，不要求字符连续。字符串保持，实现额外定义空串为0。

区间两端相等时可在内部最长回文外加这两个字符；不等时至少舍弃一端，取两种区间的较大值。left从右向左，right从左向右：best[right]更新前是上一行左端为left+1的区间，best[right-1]已是当前left的区间，inner保存上一行的右前一列。每个单字符初始化为1，空内部长度为0；更新后再把旧best[right]留作下一列inner。时间O(n^2)，额外空间O(n)。

独立oracle按位置掩码枚举每个子序列，直接与自身反转比较，不复用区间递推。三字母长度0..7的3280个串全部核对，空串为扩展。边界覆盖1000同字符、交替字符、两段不同字符、bbbab与cbbd，核对int。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
