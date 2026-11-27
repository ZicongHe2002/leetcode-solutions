# 963. Minimum Area Rectangle II · Python

[原题](https://leetcode.com/problems/minimum-area-rectangle-ii/)。

矩形对角线等长且互相平分；反过来两条不同点对若有相同中点与长度，会组成平行四边形且对角线等长，因而是矩形。用两倍中点与长度平方作整数键，不用浮点比较。对同组两条对角线，取一条的端点与另一条两端点，得到两条相邻边，绝对叉积即面积，排除零面积取最小。允许旋转，不依赖轴对齐。

N个点，配对及组内比较时间保守上界O(N^4)，存储O(N^2)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
