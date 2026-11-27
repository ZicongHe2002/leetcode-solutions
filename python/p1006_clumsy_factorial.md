# 1006. Clumsy Factorial · Python

[原题](https://leetcode.com/problems/clumsy-factorial/)。

相邻递减整数间运算按乘、除、加、减循环，乘除优先且同级从左到右。栈项表示带正负号的加法组，乘除直接更新当前组，加减开新组。原表达式中正数乘除组先取整再由减号扣除，所以栈中负项除法必须向0截断；不能直接用Python负数//向下取整。通过正整数商再恢复符号实现，不经浮点数。

时间O(n)，加法项栈空间O(n)，没有使用eval或未经解释的余数公式。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
