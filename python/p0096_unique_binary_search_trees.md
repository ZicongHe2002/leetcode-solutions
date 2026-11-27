# 96. Unique Binary Search Trees · Python

[原题](https://leetcode.com/problems/unique-binary-search-trees/)。

原题1<=n<=19，键为1..n各出现一次，返回结构不同的二叉搜索树数量。只统计结构；有序键在任一结构上按中序位置唯一确定，不额外排列标签。

counts[m]表示m个连续有序键可形成的结构数。选根后，左边left_size个键全部小于根，右边m-1-left_size个全部大于根，两边结构独立，所以该根贡献counts[left_size]*counts[m-1-left_size]。按左子树大小0..m-1求和枚举所有根，根不同的树不会重计。

counts[0]=1表示空子树是一种合法选择，而非没有选择；否则叶子和只有一侧子树的情形都会被错误乘成0。外层按节点数递增，依赖的两侧大小都更小，已计算完成。时间O(n²)，额外空间O(n)，Python整数精确保存计数；n=19结果1767263190。外部测试仅使用原题1..19。

独立小规模oracle枚举1..n的全部插入顺序，按真实BST插入所决定的左右子序列递归形成嵌套结构，并以结构去重；n=1..7共5913种插入顺序，多个顺序得到同树只算一次。另对1..19全部合法输入用Catalan闭式comb(2n,n)//(n+1)核对，覆盖最大值、int类型与重复调用。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
