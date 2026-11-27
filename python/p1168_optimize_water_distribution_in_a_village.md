# 1168. Optimize Water Distribution in a Village · Python

[原题](https://leetcode.com/problems/optimize-water-distribution-in-a-village/)。

每所房子可独立打井，或经管道从其他已有水源的房屋得到水。引入虚拟节点0，选择边(0,i)代表在房屋i花wells[i-1]打井，原管道仍为房屋间边。任何可行供水方案都使全部房屋连到0，反过来连通0的生成树也给出合法供水方案，所以问题转为n+1个节点的MST。Kruskal选择n条跨分量边即完成，井边保证始终可连通。

管道m条，时间O((n+m)log(n+m))，额外空间O(n+m)，输入井和管道均保持。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
