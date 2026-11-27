# 812. Largest Triangle Area · Python

[原题](https://leetcode.com/problems/largest-triangle-area/)。

枚举三个不同下标的点，从第一个点引出两向量，行列式绝对值是平行四边形面积，也就是三角形面积的两倍。保留整数最大值，最后除以2返回浮点数。共线点自然贡献0，方向符号由绝对值消除，不需要斜率或开方，不修改输入。

时间O(n^3)，组合生成器只保留当前三点，额外空间O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
