# 899. Orderly Queue · Python

[原题](https://leetcode.com/problems/orderly-queue/)。

k=1时只能把首字符移到末尾，可达状态恰为全部循环位移，逐个取字典序最小。k>=2时可选择前两个字符配合循环移动实现相邻次序交换，进而生成任意排列，所以排序串可达且全局字典序最小。两类操作能力不同，不能对k=1直接排序。

k=1时构造并比较n个长度n字符串，时间O(n^2)，额外空间O(n)；k>=2排序时间O(n log n)、额外空间O(n)。输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
