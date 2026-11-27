# 798. Smallest Rotation with Highest Score · Python

[原题](https://leetcode.com/problems/smallest-rotation-with-highest-score/)。

原题nums长n在1..100000，0<=nums[i]<n。左旋k后原下标i位于(i-k)模n，值<=新下标得1分；求最大分对应的最小k，只需考虑0..n-1。输入保持。

反过来统计失分。值v失分当新下标位于0..v-1，即k模n位于从i-v+1到i的连续v个位置。将它记为循环半开区间[start,end)，start=(i-v+1)%n，end=(i+1)%n。v=0从不失分，跳过；题目保证v<n，非空区间不会整圈端点相同。

用差分在start加1、end减1。start<end时是普通区间；start>end时区间跨过0，另给changes[0]加1，于是在[0,end)和[start,n)的前缀都计入该失分元素。前缀累计得到每个k的总失分，最小失分等价最大得分。按k递增扫描，仅严格变好才更新，保留同分的最小k；n=1只有值0，得到0。

建差分与扫描各O(n)，额外空间O(n)，不实际旋转n次、不修改输入。不将所有值都<n的合法合同擅自扩大到值=n。

独立oracle对每个k实际拼接左右切片，逐项直接计分，再以最大分和最小k取答案。枚举n=1..6全部合法数组共50069个；另测官方例、同分、100000长度全0/全n-1/递增/递减数组，边界答案用各自明确得分证书。检查int与输入保持，未向LeetCode提交。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
