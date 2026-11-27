# 957. Prison Cells After N Days · Python

[原题](https://leetcode.com/problems/prison-cells-after-n-days/)。

每次用旧状态同时计算新状态，内部格当且仅当两邻居相同为1，端点因缺少一侧邻居永远变0。8位状态有限且转移确定，首次重复后进入循环。history保存每个新状态出现时的序号，重复点给出周期起点与长度；剩余天数对周期取模即可定位最终状态，不假设固定周期14。n为0时直接返回原状态副本。

至多访问2^8种状态，时间O(8*min(n,2^8))，空间O(8*2^8)，原cells不修改。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
