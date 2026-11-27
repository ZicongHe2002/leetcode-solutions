# 1100. Find K-Length Substrings With No Repeated Characters · Python

[原题](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/)。

题目k为正整数。每次加入新字符后，若窗口超过k，就移除最早字符并删除零频次键。窗口长度达到k后，不同字符数恰等于k即说明没有重复。按右端位置分别计数，内容相同但出现在不同位置的合法子串仍各算一次。k大于字符串长度时没有完整窗口，返回0。

时间O(n)，额外空间O(min(n,k,字符集大小))，输入字符串保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
