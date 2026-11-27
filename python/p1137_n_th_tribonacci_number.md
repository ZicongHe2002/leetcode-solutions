# 1137. N-th Tribonacci Number · Python

[原题](https://leetcode.com/problems/n-th-tribonacci-number/)。

初值T0=0、T1=T2=1，之后每项是此前三项之和。循环开始时三个变量对应连续三项，同时赋值使右侧先用旧值求和，再把窗口整体前移。n=0、1、2分别直接按初值返回。

时间O(n)，额外空间O(1)，无指数递归或整张状态表。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
