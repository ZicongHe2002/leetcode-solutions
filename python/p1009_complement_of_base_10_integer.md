# 1009. Complement of Base 10 Integer · Python

[原题](https://leetcode.com/problems/complement-of-base-10-integer/)。

题目取反范围是n不带前导0的二进制表示，不能直接用Python的无限符号位~n。bit_length给有效位数，构造同宽全1掩码再异或，每一有效位恰翻一次，高位不产生额外1。n=0虽然bit_length为0，但题目表示为单个0，补数应为1，单独处理。

按题目有界整数操作计时间和额外空间O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
