# 1122. Relative Sort Array · Python

[原题](https://leetcode.com/problems/relative-sort-array/)。

arr2中的元素互异且属于arr1。频次表保留arr1所有重复项，按arr2顺序依次输出并删除该键，余下键就是没有指定相对次序的数值，对它们升序输出。删除键后不会把已按arr2输出的数字再次附到末尾。比如arr1=[4,2,4,1]、arr2=[4]，得到[4,4,1,2]。

arr1长n、arr2长m、不同数值D，时间O(n+m+D log D)，额外空间O(n+D)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
