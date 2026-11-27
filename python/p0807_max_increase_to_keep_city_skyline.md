# 807. Max Increase to Keep City Skyline · Python

[原题](https://leetcode.com/problems/max-increase-to-keep-city-skyline/)。

每格高度不能超过原行最大值或原列最大值，否则至少一个方向的天际线变高。将它增至两者较小值即可；这个值不会小于原高度，原来的行列最大值也不会消失。所有格子可以独立达到该上界，所以逐格差值之和就是最大增高量。输入不修改。

若网格有R行C列，时间O(RC)，额外空间O(R+C)。

按用户要求直接交付代码，未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
