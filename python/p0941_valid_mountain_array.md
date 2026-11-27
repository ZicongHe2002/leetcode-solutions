# 941. Valid Mountain Array · Python

[原题](https://leetcode.com/problems/valid-mountain-array/)。

山形要求至少三项且先严格递增后严格递减，两段都非空。先扫描所有上坡，若停在首尾就缺一段，失败；随后只允许下降，最终必须到数组尾。平台使两种严格比较都停止，多峰会让下降扫描提前停止，所以都被排除。

时间O(n)，额外空间O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
