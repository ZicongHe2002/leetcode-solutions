# 77. Combinations · Python

[原题](https://leetcode.com/problems/combinations/)。

原题1<=n<=20、1<=k<=n，返回1..n中所有k个数的组合，外部顺序任意。实现把每个组合按递增顺序输出，不重复选同一数字。

path保存已选递增前缀，下一项只从start及以后选择。还需remaining项时，本项最大只能到n-remaining+1，否则后面数字不够；range的右开界因此是n-remaining+2。每个组合只有一种递增选择路径，达到k项后复制结果，返回时恢复前缀。输出主导时间O(k*C(n,k))，辅助回溯空间O(k)，不计输出。

独立oracle直接使用itertools.combinations的组合迭代器，不复用递归或剪枝。n=1..10的全部合法k共55对核对。边界覆盖n=20且k=1/2/10/20，包括184756个长度10的组合，检查端点、输出集合及无重复，返回两层列表。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
