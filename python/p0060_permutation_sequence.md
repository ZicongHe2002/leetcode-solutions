# 60. Permutation Sequence · Python

[原题](https://leetcode.com/problems/permutation-sequence/)。

原题1<=n<=9，1<=k<=n!，返回数字1..n全部排列按字典序的第k个字符串。n<=9保证每个数字是一个字符，不能把此接口直接扩成包含多位数标签的相同字符串顺序。

先把k变成从0起算。还剩remaining个数字时，每个候选首数字占(remaining-1)!个连续排列，按这个块大小除k，商就是有序available中的下一数字下标，余数是该块内后续排名。弹出选中字后继续，最后余数0、只剩唯一数字。每一步跳过整块，不生成前面k-1个排列。

阶乘表O(n)，每次列表pop可能移动O(n)项，总时间O(n²)，额外空间O(n)。原题最大9!=362880，全部整数运算，无浮点舍入。

独立oracle用itertools.permutations按字典序枚举n=1..7的所有5913个排列，逐排名核对。最大n=9使用每位右侧较小数字数乘对应阶乘的独立排名公式回读，覆盖首尾、两个中位和多个内部k；另有n=3,k=3与n=4,k=9固定样例，验证字符集合、唯一性、str与排名。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
