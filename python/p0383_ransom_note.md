# 383. Ransom Note · Python

[原题](https://leetcode.com/problems/ransom-note/)。

原题ransomNote与magazine长度各1..100000，只含小写英文字母，每个magazine字符最多用一次，判断能否组成ransomNote，返回bool。字符顺序不限制，但重复次数必须足够。

先统计magazine可用字符数，逐字符处理目标。余量为0表示当前字符没有未用来源，立即False；否则减一，使同一来源次数不能重复使用。每个字母独立受限，所有目标字符均成功消费即充分，顺序不会改变可行性。时间O(r+m)，固定26字母表下额外空间O(1)，不修改字符串。

独立参考回溯为每个目标字符分配一个相等且未用过的magazine下标，用位集跟踪位置，不按频次公式直接判断。字母a/b、长度1..5的62种非空字符串两两组合，共3844次；另测100000长度、恰够/缺一/长度不足及来源重排，核对bool。没有在线Accepted记录。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
