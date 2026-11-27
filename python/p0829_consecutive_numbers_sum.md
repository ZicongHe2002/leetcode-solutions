# 829. Consecutive Numbers Sum · Python

[原题](https://leetcode.com/problems/consecutive-numbers-sum/)。

长度k、起点a的连续正整数和为k*a+k*(k-1)/2。枚举k，减去后面的三角数后若能整除k，就得到整数起点。循环条件k*(k+1)/2<=n正是从1开始的该长度最小和不超过n，保证求得起点至少1。不同长度描述不同序列，单个n对应k=1也计入。

长度至多O(sqrt(n))，时间O(sqrt(n))，额外空间O(1)，只做整数运算。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
