# 999. Available Captures for Rook · Python

[原题](https://leetcode.com/problems/available-captures-for-rook/)。

车只能沿同行同列走，不能穿过棋子。定位题目保证唯一的R，四个方向分别越过空格；首个白象B阻挡，首个黑兵p可捕获一次并停止，边界终止。不能把同方向后续兵也计为一次移动能捕获的目标。棋盘保持不变。

固定8x8棋盘，时间和额外空间O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
