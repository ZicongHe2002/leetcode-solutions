# 1106. Parsing A Boolean Expression · Python

[原题](https://leetcode.com/problems/parsing-a-boolean-expression/)。

题目保证表达式合法，!仅有一个参数，&与|至少有一个参数。扫描时跳过逗号，其余字符先入栈；遇到右括号，栈中直到左括号的内容已经被内层归约为t/f。取出参数和操作符，分别计算非、与、或，再把结果作为单个t/f压回栈。参数弹出顺序反转不影响与/或，非只有一个参数。单独的t或f也直接支持。

每个字符入栈和出栈至多一次，全部参数扫描次数O(n)，时间O(n)，额外空间O(n)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
