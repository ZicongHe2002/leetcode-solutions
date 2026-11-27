# 885. Spiral Matrix III · Python

[原题](https://leetcode.com/problems/spiral-matrix-iii/)。

从给定内部起点先向东，接着南、西、北，边长依次1、1、2、2、3、3。走出矩形时仍按无限网格螺旋前进，只是不收集坐标，否则在边界折返会改变题目顺序。每个无限螺旋坐标只访问一次，扩张最终覆盖整块矩形，收集到rows*cols项立即停止。

时间上界O(max(rows,cols)^2)，结果空间O(rows*cols)，除输出外额外空间O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
