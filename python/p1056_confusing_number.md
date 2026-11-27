# 1056. Confusing Number · Python

[原题](https://leetcode.com/problems/confusing-number/)。

旋转180度同时改变数字形状与数位顺序。依次取原数最低位，按0->0、1->1、6->9、8->8、9->6接到新数末尾，遇其他数字就不是合法旋转。合法后还要求新整数与原数不同；0旋转仍为0，所以不是confusing。旋转后前导0按整数表示自然消去，不误判为非法数字。

位数D，时间O(D)，额外空间O(1)，不使用浮点数。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
