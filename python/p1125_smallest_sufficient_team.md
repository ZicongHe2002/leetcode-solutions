# 1125. Smallest Sufficient Team · Python

[原题](https://leetcode.com/problems/smallest-sufficient-team/)。

所需技能最多16种，题目保证存在充分团队。给技能编号成位，某人拥有的技能用按位或合并。best[mask]保存目前已处理人员中覆盖mask的最小团队索引。每处理一个人，对更新前的状态快照决定是否加入他，防止本轮重复选取同一人。相同覆盖只留人数更少者，因为未来加入任何人时，较大团队都不会更优。输出任意一个最小团队即可，不要求字典序最小。

技能数S、人员数P、输入技能条目总数L，最优团队人数最多S；时间O(L+P*S*2^S)，索引元组及状态额外空间O(S*2^S)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
