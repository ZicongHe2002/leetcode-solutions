# 1088. Confusing Number II · Python

[原题](https://leetcode.com/problems/confusing-number-ii/)。

旋转180度只允许0、1、6、8、9。按从高位到低位生成正整数，首位不选0；把新数字追加到原数右端时，其旋转像应追加到旋转数左端，所以用image*place+rotated更新。place始终等于当前原数位数对应的10次幂，即使旋转数有前导0也不能缩短它。仅当原数与旋转数不同才计数，例如10旋转后是1，应计入；11则不计入。生成超过n就停止该层后续更大数字，零本身不计数。

设n有L位，生成节点不超过O(5^L)，每个节点固定枚举五种数字，时间O(5^L)，递归额外空间O(L)，不存储全部候选。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
