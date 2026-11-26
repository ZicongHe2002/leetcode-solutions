# 216. Combination Sum III · Python

[原题](https://leetcode.com/problems/combination-sum-iii/)。

原题2<=k<=9、1<=n<=60，从1..9中选恰好k个互异数字使和为n，返回全部组合，外部顺序任意。每个组合按递增顺序输出。

path保持递增、remaining是还需凑出的和。还需needed项时，最小可达和为从start起连续needed个数之和，最大为9起向下needed个数之和；可用数字不足或remaining落在范围外就剪枝。下一项上界为10-needed，确保后面还有足够数字。达到k项时只保存剩余和0的路径，每条递增选择唯一。候选固定9个，最坏工作O(9*2^9)，辅助回溯空间O(k)，不计输出。

独立oracle用itertools.combinations枚举1..9的k项，再直接sum筛选，不复用最小/最大和公式或递归。原题全部480对k/n均核对。另明确验证k=9总和45唯一、44或60无解、k=2的最小/最大可达和，以及多个结果，检查两层列表与无重复。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
