# 1128. Number of Equivalent Domino Pairs · Python

[原题](https://leetcode.com/problems/number-of-equivalent-domino-pairs/)。

骨牌允许旋转，[a,b]与[b,a]等价。将较小端点放前面作为唯一键，读入新骨牌时，它与此前同键的每张骨牌都形成一个新下标对，所以先把已有频次加到答案，再增加频次。这样每对只在较后骨牌出现时计一次，避免自己配自己或重复计数。例如三张同键骨牌累计新增0+1+2=3对。

期望时间O(n)，额外空间O(D)，D为不同归一键数；本题端点1..9，因此D至多45。输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
