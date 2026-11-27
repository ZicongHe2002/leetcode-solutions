# 840. Magic Squares In Grid · Python

[原题](https://leetcode.com/problems/magic-squares-in-grid/)。

三阶正常幻方恰好包含1..9，合计45，所以每行和为15，中心为5。逐个3x3窗口先检查中心和九个值集合，再检查三行、三列与两条对角线全为15，条件全部满足才计数。小于3的网格自然没有窗口，原网格中0或大于9的值由集合条件排除。

每个窗口固定九格，时间O(RC)，额外空间O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
