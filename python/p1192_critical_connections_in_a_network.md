# 1192. Critical Connections in a Network · Python

[原题](https://leetcode.com/problems/critical-connections-in-a-network/)。

无向图一条DFS树边parent-node是桥，当且仅当node子树无法经回边到达parent或更早祖先，即low[node]>discovered[parent]。发现新节点时分配时间，遍历完成才将low回传父节点。用边编号只跳过真正父边，不会把平行边误当同一边；显式迭代器栈避免十万节点深链递归溢出。答案边与列表顺序任意，输入连接不修改。

时间O(n+m)，额外空间O(n+m)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
