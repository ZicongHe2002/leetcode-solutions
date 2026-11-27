# 1010. Pairs of Songs With Total Durations Divisible by 60 · Python

[原题](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)。

两首总时长整除60等价于余数互补。扫描到当前首时，只查询此前余数为(-r)%60的歌曲数，再把当前余数频次加1，保证不同下标且每对只计一次。余数0和30与自身互补也由同一顺序处理，不会把当前首与自己配对。

时间O(n)，固定60项频次数组空间O(1)，输入保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
