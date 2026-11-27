# 173. Binary Search Tree Iterator · Python

[原题](https://leetcode.com/problems/binary-search-tree-iterator/)。

原题提供1..100000节点的BST，值0..10^6，构造BSTIterator(root)，next返回下一中序值int，hasNext返回bool且不前进。next只会在存在下一项时调用，两个方法合计至多100000次。TreeNode供本地导入，对接评测器val/left/right；实现只借用树引用，不修改树，也不预先展开全部中序值。

栈保存尚未输出的祖先路径，栈顶是下一个中序节点。构造时压入根的整条左链；next弹出栈顶后，压入其右子树的左链，从而把该节点的后继恢复到栈顶。每个节点至多压入、弹出各一次，完整遍历累计O(n)操作，next为摊销O(1)，单次最坏O(h)；hasNext只检查栈，O(1)。构造O(h)，额外空间O(h)，h为树高，最坏可达n。

测试独立按BST中序有序值作参考，并反复hasNext核对不前进。枚举1..7节点的625种BST树形，完整遍历直到hasNext=False；另测100000节点左深链和右深链，每个大样本只读前50000项，每项一次hasNext和一次next，恰好100000次方法调用，遵守上限。核对输出类型、前缀及树的所有val/left/right保持。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
