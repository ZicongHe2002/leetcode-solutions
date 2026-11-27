# 874. Walking Robot Simulation · Python

[原题](https://leetcode.com/problems/walking-robot-simulation/)。

方向顺序北东南西，-2左转减1、-1右转加1后对4取模。正命令逐单位步前进，下一格有障碍就结束本条前进命令，但后续命令仍执行。每次实际移动后更新x^2+y^2，不开方；转向不会改变距离。障碍按坐标元组存集合，负坐标与重复坐标自然处理，不修改输入。

设总要求步数S、命令数C、障碍数B，期望时间O(S+C+B)，空间O(B)。原题每个正命令不超过9，所以也可写时间O(C+B)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
