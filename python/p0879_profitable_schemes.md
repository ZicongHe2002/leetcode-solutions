# 879. Profitable Schemes · Python

[原题](https://leetcode.com/problems/profitable-schemes/)。

ways[used][earned]统计恰用used人、收益达到earned的方案，把超过minProfit的收益统一封顶到minProfit，因为以后只关心是否达标。每个犯罪可不选，原状态保留；选它就从used-people转移并增加收益。人数倒序使来源行仍是加入本项前的状态，正人数合同保证同一犯罪不重复使用。初始空方案ways[0][0]=1，最后对所有不超过n的人数的达标列求和，收益门槛0时也包含空方案。

犯罪数C、人数上限N、收益门槛P，时间O(CN(P+1))，额外空间O(N(P+1))，按10^9+7取模，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
