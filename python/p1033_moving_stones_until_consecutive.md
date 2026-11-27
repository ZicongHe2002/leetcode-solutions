# 1033. Moving Stones Until Consecutive · Python

[原题](https://leetcode.com/problems/moving-stones-until-consecutive/)。

三位置排序后，跨度2表示已连续。若某相邻间距为1或2，可以一次把另一端石子移到它们旁边或中间形成连续三格；两间距都大于2则至少两步且两步可达。最大操作数等于最外跨度中的空格数right-left-2，每步可让端点向内推进至少一格空隙，选择逐格推进能达到该上界。此题允许端石移入原最外区间，与1040的更严格移动条件分开处理。

固定三位置，时间与额外空间O(1)。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
