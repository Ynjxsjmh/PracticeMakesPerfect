int numTrees(int n) {
    /* ��������������ߵ��ӽڵ�ֵС���м�ģ��ұߴ����м��
       ���������������������������������������˷�ԭ��
     */
	if (n == 0) {
		return 1;
	}

	if (n == 1 || n == 2) {
		return n;
	}

	int result = 0;

	for (int i = 1; i <= n; i++) {
		result += numTrees(i - 1) * numTrees(n - i); // i-1 ���� i С��������������n-1 ���� i �������������
	}

	return result;
}