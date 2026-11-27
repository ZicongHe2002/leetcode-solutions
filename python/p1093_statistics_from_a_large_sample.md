# 1093. Statistics from a Large Sample · Python

[原题](https://leetcode.com/problems/statistics-from-a-large-sample/)。

count[i]表示数值i的出现次数，题目保证样本非空且众数唯一。均值用加权和除以总频次；中位数用从0开始的两个中间秩(total-1)//2与total//2。频次前缀覆盖某个秩时，把当前数值计入中位数和；奇数样本两秩相同，会计两次后除以2，偶数样本则平均两个中间值。无需展开可能极大的实际样本。

设频次数组长度为K（本题256），时间O(K)，额外空间O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
