# 1094. Car Pooling · Python

[原题](https://leetcode.com/problems/car-pooling/)。

车辆沿坐标增大方向前进，一段行程在start上车、end下车，覆盖半开区间[start,end)。把同一位置的所有变化合并后再检查载客量，自然允许先下车再接同位置的新乘客，不会因事件录入次序造成误判。每处理完一个位置，aboard恰为随后路段的乘客数，任一位置超过capacity便不可行。

行程数n，最多2n个事件位置，时间O(n log n)，额外空间O(n)，输入不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
