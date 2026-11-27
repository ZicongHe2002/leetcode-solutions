# 1005. Maximize Sum Of Array After K Negations · Python

[原题](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/)。

翻负数为正数增益为其绝对值两倍，按值升序先翻最负的，直到没有负数或操作用完。若仍有操作，所有值已非负，偶数次可对同一项翻两次抵消；奇数次必须额外翻一项，选当前最小值损失最少。存在0时额外奇数操作不损失和。只操作排序副本，精确消耗k次的效果由余数奇偶表达。

时间O(n log n)，额外空间O(n)，原数组保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
