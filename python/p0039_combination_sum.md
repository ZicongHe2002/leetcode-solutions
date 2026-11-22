# 39. Combination Sum · Python

[原题](https://leetcode.com/problems/combination-sum/)。

候选值有1..30个，彼此互异且在[2,40]，target在[1,40]，题目保证不同组合数少于150。每个值可重复使用，返回和为target的全部不同组合，顺序任意。本实现先复制排序，保留输入；组合内非递减，结果行互不共享。额外支持正值1、空候选和target=0，但不支持0或负候选值。

visit(start,remaining)只选择下标不小于start的值，追加后递归仍传index，允许重复使用当前值。path始终非递减且与remaining之和保持原target。排序后遇到value>remaining即可结束该层循环，后面的值更大。所有候选为正使remaining严格减少，递归必终止；remaining=0时复制path。任意合法组合按非递减顺序有唯一的候选下标序列，因此不会漏掉，也不会把选择顺序不同当成另一组合。

设N为候选数、L=floor(target/min(candidates))、S为实际展开的递归节点数、K为答案数。排序O(N log N)，每节点最多扫描N个候选、每答案复制至多L项，时间O(N log N+N·S+K·L)；S可随输入指数增长，不声称多项式界。不计结果的排序副本、path与递归空间O(N+L)。空候选单独是常数工作。

独立oracle枚举各候选使用次数的笛卡尔积，计算加权和并展开满足条件的次数向量，不复用递归减法。枚举2..7的全部56个长度1..4候选集合，对target=1..15共840组查询；输入顺序交替反转。边界覆盖无解、40目标、30候选、可重复使用、空候选与0目标扩展，并检查输入保持及输出行无别名。

A使用OpenAI Codex辅助编写；实际验证见PR与日志，未向LeetCode提交。完整初稿可由B正式review后按最终head普通merge，共同补写为可选，仅按真实内容署名。
