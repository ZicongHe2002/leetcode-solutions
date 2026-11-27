# 1000. Minimum Cost to Merge Stones · Python

[原题](https://leetcode.com/problems/minimum-cost-to-merge-stones/)。

每次恰合并k个相邻堆，堆数减少k-1，所以最后能成1堆必须满足(n-1)是k-1倍数。区间状态保存合并到该长度允许的最少堆数的成本；分割点每次跨k-1，使左段可成1堆，右段保留对应最少堆数。两段成本取小，若整个区间长度满足可成1堆，就再付整段总石子数，把最后k堆合为1。前缀和提供该成本，单堆基例0。

时间O(n^3/(k-1)+n^2)，空间O(n^2)，输入保持，k>=2由题目保证。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
