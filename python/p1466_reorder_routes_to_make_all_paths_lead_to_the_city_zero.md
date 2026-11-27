# 1466. Reorder Routes to Make All Paths Lead to the City Zero · Python

[原题](https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/)。

原题2..50000个城市、n-1条单向道路，其无向结构保证为树，编号0..n-1。最少反转若干道路，使每个城市都能到0，返回int，连接输入不变。

从0在无向树上遍历，原边source到target在source侧记代价1、target侧记代价0。向未处理子节点走时，代价1说明原边背离根，必须反转；代价0已经指向根，不需修改。树中每个子树到根只有这一条割边，所以背根边的反转各自必要；把它们全翻转又足以让每点沿唯一父链到0，因此求和就是最小数。树保证仅跳过parent即可避免返回与重复，不把该规则推广到含环一般图。显式栈不依赖递归深度，时间O(n)，额外空间O(n)。

独立参考枚举所有道路反转子集，对每个方向方案用反图从0检查全点可达，取最少翻转数。用Prüfer序列生成2..5节点全部标号树，再枚举每条边朝向，共2142棵有向树，逐一核对。另测50000节点外向/内向/交替长链与外向星形、原题样例，检查int与输入保持。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
