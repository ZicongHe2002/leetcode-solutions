# 378. Kth Smallest Element in a Sorted Matrix · Python

[原题](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)。

原题为n*n矩阵，1<=n<=300，每行、每列均非递减，值域-10**9..10**9，1<=k<=n*n。按所有元素含重复值的顺序求第k小，保持输入。

在最小值到最大值之间二分候选middle，计算矩阵内不大于middle的元素数count。从左下角开始逐列扫描，当前行过大时向上移动；当前列0..row全部不大于middle，计入row+1个。由于下一列只会更大，行指针不必下移，一次计数最多向右n次、向上n次，时间O(n)。

count随候选值单调不减。count>=k说明第k小不大于middle，令high=middle；否则令low=middle+1。区间持续包含第k小且严格缩短，即使middle本身不在矩阵中也不影响判定。结束时low是首个使count>=k的值，也就是第k小。若D为最大值减最小值，时间O(1+n log(D+1))，D=0时直接返回，辅助空间O(1)。

独立oracle把全部元素展开并排序，不进行值域二分。枚举元素为-1/0/1、尺寸1..3的所有行列有序矩阵，共198个，查询各自全部合法k，共1658次。边界覆盖300*300、全相等、首末排名及横跨正负极值的重复块，核对int与逐行输入保持。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
