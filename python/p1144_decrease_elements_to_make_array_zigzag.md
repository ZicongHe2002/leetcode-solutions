# 1144. Decrease Elements To Make Array Zigzag · Python

[原题](https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/)。

锯齿只有两种方向：偶数位为谷底或奇数位为谷底。固定方向后，只降低谷底，使其严格小于两侧原值，需要max(0,value-min(neighbors)+1)步。降低山峰只会让相邻谷底要求更严格，因此最优方案不必降低山峰；各谷底互不相邻，可以独立计算。边界缺失邻居视为正无穷，单元素无需移动。

时间O(n)，额外空间O(1)，不实际改动输入数组。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
