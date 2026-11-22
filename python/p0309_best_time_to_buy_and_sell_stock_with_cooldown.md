# 309. Best Time to Buy and Sell Stock with Cooldown · Python

[原题](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)。

原题prices长度1..5000，价格0..1000，同时至多持有一股，可以多次交易，但卖出后的下一整天不能买入，求最大利润，保持输入。

按每天结束时分为holding持股、sold当天刚卖出、resting不持股且当天未卖出。holding可继续持有，或从昨天的resting买入；sold只能从昨天持股卖出；resting可继续休息，或由昨天刚卖出走过今天的冷却日。三个右侧先计算再赋值，所以昨天的sold不会直接流入今天的买入，冷却限制得到保留。

最初仅resting=0合法，其余为负无穷。每天三个状态分别枚举最后动作，结束只能选resting或sold，不能把仍持有的股票当成现金利润。时间O(n)，辅助空间O(1)。

独立oracle递归枚举每天休息、买入和卖出；卖出明确给下一天设置禁止买入标志，再过一天清除，不复用三状态递推。3种价格、长度1..7的3279个数组核对。边界覆盖5000天、交替价格与三日冷却节奏、全零、下降、单日，核对int与输入保持。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
