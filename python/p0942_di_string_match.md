# 942. DI String Match · Python

[原题](https://leetcode.com/problems/di-string-match/)。

未用数字始终是连续区间[low,high]。I处取最小值，保证下一次无论取哪一剩余值都更大；D处取最大值同理保证下一值更小。取后缩对应端点，不重复也不遗漏数字，处理完N个关系后还剩一个值补尾，得到0..N的合法排列。

时间O(n)，输出空间O(n)，除输出外额外空间O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
