# 914. X of a Kind in a Deck of Cards · Python

[原题](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/)。

每组大小X相同且全是同牌面，故X必须整除每个牌面出现次数；有一个X>=2可行当且仅当全部频次的最大公约数至少2。逐频次求gcd，达到1后再加入其他频次也不可能变大，可提前失败。只看总牌数的因子不足以保证每个牌面都能分整组。

N张牌U种值，时间O(N+U log N)，额外空间O(U)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
