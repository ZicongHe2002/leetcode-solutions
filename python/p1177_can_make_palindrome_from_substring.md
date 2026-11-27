# 1177. Can Make Palindrome from Substring · Python

[原题](https://leetcode.com/problems/can-make-palindrome-from-substring/)。

题目允许对子串任意重排并替换至多k个字符，查询不改变原串。回文中最多一种字符频次为奇数，若当前有o种奇频字符，一次替换可把两种奇频字符配平，所以最少需要floor(o/2)次。用26位掩码记录前缀频次奇偶，闭区间[left,right]的掩码由prefix[right+1]异或prefix[left]得到，统计置位数即可。

固定26字母下时间O(n+q)，额外空间O(n+q)，不复制每个查询子串。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
