# 1136. Parallel Courses · Python

[原题](https://leetcode.com/problems/parallel-courses/)。

每学期可同时修任意数量课程，但先修课必须在更早学期完成。零入度课程构成本学期可修集合，固定每轮队列长度处理，刚解锁的课程留到下一学期，不会错误地在同学期连修先修链。每轮尽可能修完全部可修课不会推迟其他课程，因此得到最小学期数。若拓扑遍历不能覆盖n门课，存在先修环，无解。

时间和额外空间O(n+m)，m为先修关系数，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
