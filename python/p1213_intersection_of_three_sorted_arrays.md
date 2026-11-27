# 1213. Intersection of Three Sorted Arrays · Python

[原题](https://leetcode.com/problems/intersection-of-three-sorted-arrays/)。

三个数组各自严格递增。三值相等时加入一次并同时推进；否则当前最小值小于至少另一个数组当前值，该数组未来值只会更大，最小值已不可能成为共同元素，因此所有持有该最小值的指针都可安全前进。任一数组耗尽后不再有新交集，输出自然递增。

时间O(n1+n2+n3)，除输出外额外空间O(1)，不使用集合或修改输入。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
