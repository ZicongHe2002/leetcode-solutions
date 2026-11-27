# 873. Length of Longest Fibonacci Subsequence · Python

[原题](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/)。

严格递增且值唯一，使最后两项arr[j],arr[k]所需前项arr[k]-arr[j]最多对应一个下标i。若i<j，就把以(i,j)结尾的最长长度加1；不存在更早三项记录时，任意二元组长度基例为2。按最后下标递增处理，所需前状态总已可用。只在形成三项时更新best，因此无斐波那契子序列返回0。

时间O(n^2)，额外空间O(n^2)，输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
