# 1198. Find Smallest Common Element in All Rows · Python

[原题](https://leetcode.com/problems/find-smallest-common-element-in-all-rows/)。

每行严格递增且矩阵非空。共同元素一定属于首行，按首行顺序尝试，首次在所有行中查到的值就是最小共同值。二分插入点既需未越界，也需实际等于候选，不能把插入位置误当命中。没有候选满足时返回-1，只有一行时返回该行最小值。

R行C列，时间O(RC log(C+1))，当前实现每轮mat[1:]行引用切片额外空间O(R)，不修改矩阵。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
