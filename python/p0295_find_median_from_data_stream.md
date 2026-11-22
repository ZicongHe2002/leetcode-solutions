# 295. Find Median from Data Stream · Python

[原题](https://leetcode.com/problems/find-median-from-data-stream/)。

原题接口为MedianFinder()、addNum(num)、findMedian()，不是Solution。插入值范围-100000..100000；每个实例的插入和查询总共至多50000次，调用findMedian前保证已有元素。addNum返回None，findMedian返回数值中位数；空结构查询不在接口合同内。

lower通过负号模拟最大堆，保存较小一半；upper为最小堆，保存较大一半。保持lower的每个值不大于upper的每个值，并让lower数量等于upper或比upper多1。插入时先进入lower，再把lower的最大值移到upper，保证跨堆顺序；若upper变多，再把upper最小值移回lower，恢复数量不变量。

奇数个元素时中位数为lower最大值，偶数时为两个堆顶的平均值。查询只读堆顶，不弹出或重排元素；奇数查询也返回float。插入O(log(m+1))、查询O(1)，m个已插入元素的辅助空间O(m)。

独立oracle对每个流前缀调用标准库statistics.median，不使用双堆。3种数值、长度1..6共1092个流，在全部6015个前缀核对；每个实例均先插入再查询。另有递增流、极值交替流两个各25000次插入加25000次查询的最大调用数用例，期待值由等差序列或正负对称直接确定，覆盖奇偶中位数与最大正负值。没有测试空结构的非法查询。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
