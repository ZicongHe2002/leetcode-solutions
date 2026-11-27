# 837. New 21 Game · Python

[原题](https://leetcode.com/problems/new-21-game/)。

分数小于k才继续抽1..maxPts，达到k后停止。到达score的概率是前maxPts个仍可抽牌状态概率之和除以maxPts，用滑动窗口维护该和。新分数小于k就加入窗口，达到k则只累加到最终答案，不能再产生后继。每步移出超过抽牌跨度的旧状态。

k=0时从0立即停止，返回1；最终最高分为k-1+maxPts，n覆盖它时也必为1；n<k则不可能以不超过n的分数停止。其余情况计算到n即可，因为分数只增加。时间O(n)，额外空间O(n)，使用浮点概率。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
