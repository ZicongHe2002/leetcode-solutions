# 920. Number of Music Playlists · Python

[原题](https://leetcode.com/problems/number-of-music-playlists/)。

ways[used]是当前长度恰好出现used种歌的合法列表数。下一首首次出现时，来源有used-1种歌，还可选n-used+1首新歌；重播时保持used种歌，最近k首都不能选，若used>k还有used-k首可用。两类末首来源不重叠，合并后按10^9+7取模。初始空列表仅一种，最终只取used=n确保每首至少出现一次。

时间O(goal*n)，滚动额外空间O(n)，不枚举具体歌曲排列。

按用户要求未编写或运行测试，未执行详细验证，未向LeetCode提交。A使用OpenAI Codex辅助编写，待B正式Code review。
