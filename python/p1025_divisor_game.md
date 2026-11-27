# 1025. Divisor Game · Python

[原题](https://leetcode.com/problems/divisor-game/)。

n=1没有小于自身的正除数可减，是败态。对正数归纳：偶数可取除数1，减后为奇数；奇数的每个除数都为奇数，减后只能交出偶数。于是所有偶数有一步进入败态，所有奇数只能进入胜态，先手获胜当且仅当n为偶数。这个返回值是由题目合法动作推导，不是常量占位。

时间与额外空间O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
