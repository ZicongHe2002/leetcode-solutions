# 982. Triples with Bitwise AND Equal To Zero · Python

[原题](https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/)。

三下标有顺序且允许相同，先枚举全部有序前两项，统计其按位与mask的次数。对该分布做按位子集和变换，得到subset[mask]为所有子掩码分布之和。第三项v要求前两项与值不能含v的任何1位，等价于它是固定位宽补掩码full^v的子掩码，因此直接查询并按每个第三下标累计。全0输入位宽0、数组大小1，也能直接计n^3。

N项、最大位宽B<=16，时间O(N^2+B*2^B)，额外空间O(2^B)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
