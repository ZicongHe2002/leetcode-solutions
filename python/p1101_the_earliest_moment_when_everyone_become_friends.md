# 1101. The Earliest Moment When Everyone Become Friends · Python

[原题](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/)。

题目至少有两个人，认识关系按图连通性传递。日志按时间升序处理，每次连接两个原本不同的分量才把groups减一，重复关系不改变分量数。当groups首次为1时，所有人已经处于同一个认识网络，当前时间就是最早时刻；日志用尽仍未连通就返回-1。并查集使用路径压缩和按大小合并。

人数n、日志m，时间O(m log m+(n+m)alpha(n))，额外空间O(n+m)，其中日志排序使用新列表，不改变原日志次序。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
