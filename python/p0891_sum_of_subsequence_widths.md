# 891. Sum of Subsequence Widths · Python

[原题](https://leetcode.com/problems/sum-of-subsequence-widths/)。

每个非空子序列宽度是最大值减最小值，只依赖选中的元素多重集，排序不改变全部按下标选取的方案总和。排序位置i作为最右被选位置时，左侧i项任意选，共2^i种；作为最左被选位置时，共2^(n-1-i)种。逐位置累计净贡献，并把第二部分反向配对到相同的2^i，得到(values[i]-values[n-1-i])*2^i。重复值仍按各自下标计，最终模10^9+7。

时间O(n log n)，排序副本空间O(n)，扫描额外空间O(1)，输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
