# 864. Shortest Path to Get All Keys · Python

[原题](https://leetcode.com/problems/shortest-path-to-get-all-keys/)。

同一位置持有不同钥匙时后续可通行范围不同，因此状态必须包含行列与钥匙位掩码。先读取起点和实际存在钥匙集合，BFS每次走一格：墙不能过，锁需要对应位，钥匙把该位置加入集合。集齐全部实际钥匙时第一次出队的距离最小；耗尽返回-1。按字母固定对应位，不依赖扫描时钥匙恰好连续编号。

R行C列、K把钥匙，最多RC*2^K个状态，时间与额外空间O(RC*2^K)，不修改输入。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
