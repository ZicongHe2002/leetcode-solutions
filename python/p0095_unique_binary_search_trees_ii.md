# 95. Unique Binary Search Trees II · Python

[原题](https://leetcode.com/problems/unique-binary-search-trees-ii/)。

原题1<=n<=8，返回键1..n各一次的全部不同BST，顺序任意。TreeNode本地定义与评测器的val/left/right一致；对接已有TreeNode的评测器时可只保留Solution及标准库导入。实现选择让所有返回树各自拥有节点，不共享可变子树，便于分别修改结果；这是本实现的额外保证。

先按节点数缓存不可变树形。大小size的根可有left_size=0..size-1个左节点，左右形状独立组合，空树形用None表示。每个组合保存(left_size,left_shape,right_shape)，不同根位置或子树形状对应不同结构，因此完整且不重复。

再为每个完整树形单独实例化节点。若本子树键从start开始，根值就是start+left_size，左边继续从start编号，右边从根值+1开始；归纳得到中序恰为1..n。缓存仅共享不可变描述，不缓存TreeNode，实例化每次都建新对象，所以不同结果及不同调用之间没有节点别名。

令C_n为n节点BST数量，输出需要n*C_n个节点，时间及含输出的总空间均为O(n*C_n)。缓存树形占O(C_n)，实例化递归深度O(n)，原题n<=8；没有把输出生成成本写成O(C_n)。

独立oracle枚举1..n的全部插入顺序，按BST左右分区得到带值结构并去重，不复用缓存树形生成。n=1..8全部46233个插入顺序覆盖2055棵不同输出树；逐节点验证共15521个对象无环、跨树无共享，结构集合及值完整一致。另核对修改旧结果不影响同批其他树或后续调用。

A使用OpenAI Codex辅助编写；实际验证见日志，未向LeetCode提交。提交后须由B正式review；仅按真实内容署名。
