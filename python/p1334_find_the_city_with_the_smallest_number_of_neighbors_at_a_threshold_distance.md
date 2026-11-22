# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance · Python

[原题](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/)。

原题n为2..100、无向边至少一条且端点对互异，权重与distanceThreshold均为1..10000。统计每座城到其他城市的最短距离不超过阈值者有多少，选数量最少者，平局选编号最大，返回int，输入保持。

Floyd按via逐个开放允许的中间节点，任意最短路径要么不经via，要么由source到via和via到target两段组成，取较小值得到全部最短距离。对角0、双向边初始化，10^9作为不可达哨兵，高于合法简单路径至多99*10000的长度；非负权重不会通过哨兵加法生成假短路。计数排除自身，使用<=包含阈值恰相等的邻城。编号升序扫描遇到count<=fewest时更新，等数必留下最大编号。时间O(n^3)，额外空间O(n^2)。

独立参考为每座城市单独运行优先队列最短路，再以(邻居数,负编号)选最小，不用Floyd递推。2..4节点的非空边图，每对可无边或权1/3，共756图，分别测试6个阈值共4536次；另测100节点、4950边完全图、10000权重、阈值边界、隔离最小编号城与原题平局样例，核对int与输入保持。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
