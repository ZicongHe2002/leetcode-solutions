# 823. Binary Trees With Factors · Python

[原题](https://leetcode.com/problems/binary-trees-with-factors/)。

数组值互异且都大于1，内部节点值必须等于两孩子值的乘积。按值排序后，任何非叶根的两个因子都严格小于根，已有子树计数可用。每个根先计单节点树1种，再枚举左因子；能整除且右因子已出现时，加上两边子树数的乘积。左右有顺序，异因子会在枚举另一左因子时再计相反排列，同因子只枚举一次。各根计数求和并按10^9+7取模。

时间O(n^2)，额外空间O(n)，排序副本不修改输入。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
