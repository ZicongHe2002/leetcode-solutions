# 279. Perfect Squares · Python

[原题](https://leetcode.com/problems/perfect-squares/)。

原题整数n在[1,10000]，返回总和为n所需的最少完全平方数个数，同一平方数可重复使用。本实现额外定义n=0返回0，不承诺负数。

counts[value]表示构成value的最少项数。任一最优表示都有某个最后平方数square，去掉它留下value-square的表示，所以枚举最后项并取counts[value-square]+1的最小值。所有平方数为正，依赖下标严格更小，按value递增即可；counts[0]=0，且平方数1保证每个状态可达。用isqrt生成平方数避免浮点边界。时间O(n·sqrt(n))，额外空间O(n)。

独立oracle从和0出发，把加一个平方数视为单位边，用广度优先最短路找n，不复用最小值递推。逐一核对n=0..200共201个值，其中0是扩展；边界覆盖10000、9999、9998、1和贪心先取最大平方数会失效的12。返回int类型也被检查。

A使用OpenAI Codex辅助编写；实际验证见PR与日志，未向LeetCode提交。完整初稿可由B正式review后按最终head普通merge，共同补写为可选，仅按真实内容署名。
