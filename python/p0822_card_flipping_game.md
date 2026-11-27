# 822. Card Flipping Game · Python

[原题](https://leetcode.com/problems/card-flipping-game/)。

若某张牌两面都是x，无论怎么翻它，正面总有x，所以x不可能成为背面出现而正面不出现的好数。反过来，若x没有出现在任何双面相同的牌上，所有含x的牌都能把x转到背面，且至少一张含x的牌提供该背面值，因此x可行。先收集不可行值，再扫描全部正反面取最小可行值，无则返回0。

时间O(n)，额外空间O(n)，不修改两输入数组。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
