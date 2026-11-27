# 893. Groups of Special-Equivalent Strings · Python

[原题](https://leetcode.com/problems/groups-of-special-equivalent-strings/)。

允许只在同奇偶下标之间交换，所以两类位置的字符多重集各自保持。反过来，同奇偶任意交换能实现该组位置的任意排列，因此偶位置排序文本与奇位置排序文本共同构成完整等价签名。把签名放集合，大小就是组数，重复词只属于同一组。

W个词、每词长度L，时间O(WL log L)，签名存储空间O(WL)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
