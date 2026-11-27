# 1089. Duplicate Zeros · Python

[原题](https://leetcode.com/problems/duplicate-zeros/)。

数组长度保持不变，每个0复制一次，尾部溢出部分丢弃。先把写指针放到完整扩展后的虚拟末尾，逆序读原数组；每项写一次，零再多写一次，仅对落在原数组范围内的位置赋值。写指针始终不早于尚未读取的位置，因此不会破坏后续读取。比如[1,0,2]原地变为[1,0,0]。

时间O(n)，额外空间O(1)。按题目要求原地修改arr，方法不返回新数组。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
