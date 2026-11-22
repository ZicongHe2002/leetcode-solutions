# 1905. Count Sub Islands · Python

[原题](https://leetcode.com/problems/count-sub-islands/)。

原题两个同形二元网格，1..500行列，四邻陆地形成岛，统计grid2中被grid1某一整岛包含的岛屿数。不是统计覆盖格数，两张输入均保持。

逐片遍历grid2的四邻连通分量，用covered记录该岛所有格是否也在grid1为陆地。若全是陆地，grid2内部连通路径同样存在于grid1，所以这些格必属于grid1同一个岛，不需额外编号grid1各岛。整片完成后covered仍True才加1。

发现某格在grid1是水，只能把covered置False，仍须继续遍历并标记该grid2岛的其余格。提前退出会把剩余部分误当新岛、重复计数。seen入队时设置，每格只处理一次。时间O(mn)，额外空间O(mn)，不修改任何网格。

独立oracle只对grid2相邻陆地做并查集合并，得到根集合；再按grid1水格给对应根标坏，答案为全部根减坏根，不复用逐岛队列与covered。两张小二元网格全部8484对逐一核对。最大500x500整岛被全覆盖得1、单个内部缺口使整岛得0、棋盘格125000个独立小岛得125000，核对int和双输入保持。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
