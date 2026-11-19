# 35. Search Insert Position · Python

[原题](https://leetcode.com/problems/search-insert-position/)给严格递增整数数组和target，返回已有值下标，或保持顺序时应该插入的位置。`Solution.searchInsert`不修改输入，返回值可以等于数组长度；空输入返回0是自然扩展。

把答案统一定义成第一个不小于target的位置。半开搜索区间为[left,right)，但候选答案边界还包括right。循环入口时，left之前的值全部小于target，right及之后的值全部不小于target。若中点值小于target，可排除中点及其左侧，令left=middle+1；否则中点仍可能是答案，令right=middle。

每轮严格缩小区间，left==right时两侧约束共同确定唯一插入边界。无需找到相等值后另外处理缺失情况，也不能把查找失败统一返回−1：例如[1,3]查找2应返回1。每次区间至多约减半，时间O(log n)，额外空间O(1)。

测试枚举−3至3的全部128个严格有序子集，对每个检查−4至4的9个target，共1152次；以线性统计小于target的元素数量作为独立oracle，核对插入后有序及输入不变。实际运行结果记录在PR，没有LeetCode Accepted。A实现，OpenAI Codex辅助整理。

## B补写：元素区间与答案边界

取nums=`[1,3,5,7]`。每行是一次实际循环的入口与更新，最终结果表示插入边界。

| target / 场景 | left | right | middle / 值 | 更新 |
| --- | --- | --- | --- | --- |
| 0，首值之前 | 0 | 4 | 2 / 5 | right=2 |
| 0 | 0 | 2 | 1 / 3 | right=1 |
| 0 | 0 | 1 | 0 / 1 | right=0，返回0 |
| 4，两值之间 | 0 | 4 | 2 / 5 | right=2 |
| 4 | 0 | 2 | 1 / 3 | left=2，返回2 |
| 7，命中 | 0 | 4 | 2 / 5 | left=3 |
| 7 | 3 | 4 | 3 / 7 | right=3，返回3 |
| 9，尾值之后 | 0 | 4 | 2 / 5 | left=3 |
| 9 | 3 | 4 | 3 / 7 | left=4，返回4 |

被访问的元素在半开区间`[left,right)`，而答案是元素之间的边界，候选在闭区间`[left,right]`。所以初始right=n即使不是合法元素下标，也必须保留为合法答案；当所有元素都小于target，正确位置正是n。若中点大于等于target，中点自身仍可能为首个不小于的位置，必须保留right=middle，不能改成middle-1。例如`[1,3]`找3时首轮middle=1，若错误设置right=0，就会返回0。

对长度d=right-left>0，middle位于区间内。更新right=middle时新长度至多d-1；更新left=middle+1也严格缩短；最终left=right时，它之前全部小于target，它之后（含该位置若存在）全部不小于target，边界唯一。没有“查找失败”分支：上表0、4、9均不存在于数组中，却分别有合法插入下标0、2、4，统一返回-1会丢失需求。

B实际补写状态表、边界证明与错误更新反例；测试执行事实在PR记录，未声称LeetCode Accepted。
