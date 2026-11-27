# 1206. Design Skiplist · Python

[原题](https://leetcode.com/problems/design-skiplist/)。

接口为Skiplist。所有层保持有序，底层包含每次插入的独立节点，因而重复值不会被丢弃。从最高层向下寻找严格小于目标的前驱，得到每层更新位置。插入塔高以1/2概率逐层延伸，删除只移除底层第一个目标节点在各层的同一对象，不会把其他重复值一起删掉。32层覆盖本题操作规模，随机仅影响性能，不影响搜索和删除正确性。

本题规模下操作期望O(log N)，最坏O(N)；节点塔总空间期望O(N)，不宣称最坏对数保证。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
