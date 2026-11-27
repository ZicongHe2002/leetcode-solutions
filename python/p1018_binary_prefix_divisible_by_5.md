# 1018. Binary Prefix Divisible By 5 · Python

[原题](https://leetcode.com/problems/binary-prefix-divisible-by-5/)。

二进制末尾追加bit会把旧值乘2再加bit，模5与这两种运算相容，所以只保存余数即可判断全部前缀。包括只由0组成的前缀，其值0也可整除5。输出布尔列表，不构造长度不断增加的大整数，也不修改输入位数组。

时间O(n)，输出空间O(n)，除输出外额外空间O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
