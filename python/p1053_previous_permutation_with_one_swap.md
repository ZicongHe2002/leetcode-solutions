# 1053. Previous Permutation With One Swap · Python

[原题](https://leetcode.com/problems/previous-permutation-with-one-swap/)。

要使单次交换后字典序小于原序且尽量大，最早改变位置应尽量靠右，因此找最右下降支点。其右后缀非递减，从末尾找最大且严格小于支点的值。该值重复时选最左出现，使被换过去的较大支点尽早出现在后缀，得到更大结果。全非递减序列没有单交换可变小，返回副本不变。

时间O(n)，结果副本O(n)，除输出外额外空间O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
