# 1001. Grid Illumination · Python

[原题](https://leetcode.com/problems/grid-illumination/)。

灯照亮同行、同列、row-column相同主对角线与row+column相同副对角线。先把重复灯坐标去重，四类频次各计实际唯一灯。查询先看任一类计数是否正，再检查自身及八邻格，把仍开着的灯移除并扣四类频次，避免重复关闭。网格可很大，始终只存实际灯与线，不建n*n矩阵。越界邻坐标不在合法灯集合，自动无操作。

L个输入灯、Q次查询，期望时间O(L+Q)，空间O(L+Q)包含输出，原lamps与queries保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
