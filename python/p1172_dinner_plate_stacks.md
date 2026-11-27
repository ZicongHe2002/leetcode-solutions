# 1172. Dinner Plate Stacks · Python

[原题](https://leetcode.com/problems/dinner-plate-stacks/)。

接口为DinnerPlates，capacity为正。push必须选择最左未满栈，pop选择最右非空栈，popAtStack只操作指定下标。未满栈索引放入最小堆，只有从满变为未满时才新增许可，避免重复索引。尾部空栈立即裁掉，堆中指向已裁掉位置的索引在后续push时惰性清理。仅在堆中没有有效未满栈时才创建新栈，因此旧尾部索引不会与新栈重复登记。

设操作数Q、当前元素数E，堆操作和裁剪摊还每次O(log Q)，空间O(E+Q)。单次操作可能清理多个过期索引或空栈，不宣称单次最坏常数。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
