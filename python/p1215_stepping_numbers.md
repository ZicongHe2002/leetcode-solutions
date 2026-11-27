# 1215. Stepping Numbers · Python

[原题](https://leetcode.com/problems/stepping-numbers/)。

踏步数相邻十进制位差的绝对值为1。单个数字均合法，0单独处理以免产生前导0。从1..9入队，每次只追加末位减1或加1的合法数字，因此不会生成不合法候选或重复数。BFS先较短位数，再按递增父值及较小末位扩展，结果自然按数值升序，保留[low,high]内项。

设不超过high的非零踏步数数量为S，时间和额外空间O(S)，不扫描整个整数区间。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
