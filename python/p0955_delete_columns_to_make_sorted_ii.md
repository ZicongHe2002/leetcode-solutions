# 955. Delete Columns to Make Sorted II · Python

[原题](https://leetcode.com/problems/delete-columns-to-make-sorted-ii/)。

本题要求删列后整行按字典序有序，不是944的各列独立有序。相邻行对若前面某个保留列已严格小于，后续字符再逆序也不影响该对。只对前缀仍相等的未决行对检查当前列：出现逆序必须删，否则可安全保留，并把严格小于的行对标为已确定。保留安全列只会减少未来约束，不会增加所需删除数，因此贪心最优。

R行C列，时间O(RC)，额外空间O(R)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
