# 1014. Best Sightseeing Pair · Python

[原题](https://leetcode.com/problems/best-sightseeing-pair/)。

得分values[i]+values[j]+i-j可拆为两项。扫描右端j时，left_best是此前i<j的最大values[i]+i，用它更新当前配对分数，再把j作为未来左端候选加入。更新顺序保证不把一个景点与自身配对。原题正值且至少两项，初始答案0不会压过合法最优正分。

时间O(n)，额外空间O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
