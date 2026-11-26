# 714. Best Time to Buy and Sell Stock with Transaction Fee · Python

[原题](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)。

原题prices长度1..50000，1<=价格<50000，0<=fee<50000，同时至多持有一股，完成每次买卖收取一次手续费，求最大利润，保持输入。

cash表示当天结束不持股的最大现金，holding表示持股的最大现金。新cash可以保持旧现金，或从昨天持股卖出并扣除一次fee；新holding可以继续持股，或从昨天cash支付买价。右侧表达式同时计算，两个状态都读取前一天值。手续费只在卖出时扣一次，不在买入和卖出两边重复收取。

初始cash=0、holding为负无穷，允许完全不交易。每天保留等待和当前合法动作的最大值，最终cash已枚举全部不持股策略。时间O(n)，辅助空间O(1)，没有价格切片副本。

独立oracle递归枚举每天休息/买入/卖出，并在实际卖出动作扣费，不复用两状态滚动公式。3种正价格、长度1..7的3279个数组，各测5种手续费，共16395次查询。边界覆盖50000天、手续费0或抵消全部价差、接近价格上限的交替、单日与典型需要合并持有区间的案例，核对int及输入保持。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
