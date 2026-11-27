# 1104. Path In Zigzag Labelled Binary Tree · Python

[原题](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/)。

第d层的标签范围为[2^d,2^(d+1)-1]，但相邻层编号方向相反。将当前标签在本层区间镜像，再整除2，恰好抵消下一层方向变化并得到父标签。不断记录并向父移动，根1的下一步得到0终止；记录顺序为目标到根，最后反转。例如14的父标签为(8+15-14)//2=4，4的父标签为3，最终路径[1,3,4,14]。

在题目有界整数模型下，时间O(log label)，输出空间O(log label)，额外状态O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
