# 917. Reverse Only Letters · Python

[原题](https://leetcode.com/problems/reverse-only-letters/)。

题目字符范围内isalpha识别英文字母，左右指针遇到非字母只跳过、不搬动该位置。两边都指向字母才交换并向内移动，因此所有非字母下标保持，字母子序列恰好反转。大小写作为原字符随交换保留。

时间O(n)，结果构造空间O(n)，指针额外空间O(1)，输入字符串保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
