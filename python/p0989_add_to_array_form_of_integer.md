# 989. Add to Array-Form of Integer · Python

[原题](https://leetcode.com/problems/add-to-array-form-of-integer/)。

从num最低位开始，carry初始为整个k，每轮把当前数组位加进来，再除以10：余数是结果当前位，商保留为下一位进位。数组位用完后若carry仍非0就继续输出，反之仍要处理剩余数组位。结果先逆序生成再反转，不把可能很长的数组形式整数整体转为十进制字符串或大整数。

数组长N、k位数D，时间和结果空间O(N+D)，输入num保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
