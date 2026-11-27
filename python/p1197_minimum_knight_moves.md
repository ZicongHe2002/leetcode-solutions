# 1197. Minimum Knight Moves · Python

[原题](https://leetcode.com/problems/minimum-knight-moves/)。

棋盘无限大，可关于坐标轴及对角线对称，先令x>=y>=0。每步单坐标最多推进2、两坐标曼哈顿距离最多推进3，因此步数至少ceil(x/2)和ceil((x+y)/3)。骑士每步翻转格子颜色，步数与x+y奇偶必须一致，必要时在下界上再加1。除近原点的(1,0)需3步、(2,2)需4步之外，这个修正下界可由骑士路径达到；原点得到0。公式依赖无限棋盘，不适用于有障碍或有限边界棋盘。

题目有界整数模型下，时间和额外空间O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
