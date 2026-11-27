# 1002. Find Common Characters · Python

[原题](https://leetcode.com/problems/find-common-characters/)。

公共字符要保留重复次数，某字符最多能共同出现的次数是所有词中频次的最小值。Counter交集逐键取最小值，依次合并后用elements按频次展开结果。某词缺少的字符频次0，会被移除；仅做字符集合交集会丢失重复数量。输出顺序任意，输入词表保持。

总字符数L，时间O(L)，除输出外额外空间O(26)，按小写字母合同计。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
