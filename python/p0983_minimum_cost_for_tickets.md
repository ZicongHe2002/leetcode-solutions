# 983. Minimum Cost For Tickets · Python

[原题](https://leetcode.com/problems/minimum-cost-for-tickets/)。

best[i]表示覆盖从第i个旅行日到末尾的最低成本。首个未覆盖日一定需有一张票覆盖，考虑从该日开始买1、7、30日票不会比更早开始覆盖更少未来旅行。有效日期为[start,start+duration)，用bisect_left找首个达到右开边界的旅行日，再加其最优后缀成本。逆序计算确保所有后继已知，尾哨兵成本0。

N个旅行日，时间O(N log N)，额外空间O(N)，输入已升序且保持不变。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
