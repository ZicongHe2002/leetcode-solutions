# 1102. Path With Maximum Minimum Value · Python

[原题](https://leetcode.com/problems/path-with-maximum-minimum-value/)。

路径从左上到右下，只能沿上下左右移动，分数为路径上最小格值而非路径和。使用最大堆保存候选路径的瓶颈分数，扩展到相邻格时，新分数为当前分数与格值的较小者。因为扩展不可能提高分数，某格首次出堆时已经具有最优瓶颈值，之后的重复候选可跳过。终点首次出堆即得到全局最优分数，起终点格值都包含在瓶颈中。

R行C列，网格边数O(RC)，时间O(RC log(RC))，额外空间O(RC)。原矩阵不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
