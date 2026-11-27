# 877. Stone Game · Python

[原题](https://leetcode.com/problems/stone-game/)。

状态为当前行动者在剩余区间能取得的最大净分差。取左端后，对手在余区间取得的净优势必须从当前拿到的石子中减去，取右端同理，两者取大。单堆基例是该堆石子数。按区间长度递增、左端递增覆盖一维表，best[left+1]与尚未覆盖的best[left]分别是两个长度少1的子问题。最终正分差表示先手能赢。

时间O(n^2)，额外空间O(n)，输入不修改。没有把对手行为当成随机选择。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
