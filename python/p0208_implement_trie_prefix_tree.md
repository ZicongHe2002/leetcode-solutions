# 208. Implement Trie (Prefix Tree) · Python

[原题](https://leetcode.com/problems/implement-trie-prefix-tree/)。

原题接口Trie()、insert(word)、search(word)、startsWith(prefix)，单词和前缀均为1..2000个小写字母，总调用至多30000次。insert返回None，另两个接口返回bool；完整单词查找与仅前缀存在必须区分。

每层字典用字母映射到下一层，沿字符路径找到对应前缀。None键只作单词结束标记，不会与原题小写字母键冲突。插入仅创建缺少的边，末端设置结束标记；重复插入同词不改变成员关系。search还需要结束标记，startsWith只需要整条路径存在，所以插入apple后app前缀存在但还不是完整单词。

所有路径操作均迭代执行，2000字符输入不依赖递归深度。长度L的插入/查找时间O(L)，存储与已插入不同前缀的总字符数成正比。

独立oracle仅保存完整字符串集合，完整查找使用集合成员关系，前缀查找使用字符串startswith。9种动作、长度0..4的全部7381个短程序核对。另一个实例恰30000次调用，包含2000字符单词及其非完整前缀、9998种短词和不存在的长词，核对None/bool返回。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
