# 1086. High Five · Python

[原题](https://leetcode.com/problems/high-five/)。

题目保证每个学生至少有五项成绩。为每个学生维护容量五的小根堆，堆未满就加入；满后仅当新成绩超过当前第五名时替换堆顶。这样处理任意前缀后，堆中始终保留该学生迄今最高五项。最后按学生编号升序输出，平均值使用整数除法。

成绩条数N、学生数S，时间O(N+S log S)，堆容量固定五，额外空间O(S)。输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
