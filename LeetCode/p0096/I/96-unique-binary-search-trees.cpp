int numTrees(int n) {
    /* 二叉搜索树：左边的子节点值小于中间的，右边大于中间的
       左子树的种类乘以右子树的种类就是总数——乘法原理
     */
	if (n == 0) {
		return 1;
	}

	if (n == 1 || n == 2) {
		return n;
	}

	int result = 0;

	for (int i = 1; i <= n; i++) {
		result += numTrees(i - 1) * numTrees(n - i); // i-1 个比 i 小的数做左子树；n-1 个比 i 大的数做右子树
	}

	return result;
}