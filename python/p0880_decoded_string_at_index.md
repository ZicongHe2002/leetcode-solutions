# 880. Decoded String at Index · Python

[原题](https://leetcode.com/problems/decoded-string-at-index/)。

数字表示把此前整段重复若干次，不是只重复前一个字母。正向只维护长度，字母加1、数字乘该数。逆向遇到重复时，第k位可按重复前长度取模映回前缀；用余数0表示该段最后一位。遇到字母且k正指段末时返回该字母，否则移除末字母，继续逆推。输入保证k在实际解码范围内。

按整数算术计，时间O(编码长度)，额外空间O(1)，不分配解码字符串。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
