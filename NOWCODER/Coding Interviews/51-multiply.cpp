/*
  B0     1   A1 A2 .. An-2 An-1
  B1     A0  1  A2 .. An-2 An-1
  B2     A0  A1 1  .. An-2 An-1
  ..     A0  A1 A2 1  An-2 An-1
  Bn-2   A0  A1 A2 .. 1    An-1
  Bn-1   A0  A1 A2 .. An-2 1
 */


vector<int> multiply(const vector<int>& A) {
    vector<int> result(A.size(), 1);

    for (int i = 1; i < A.size(); i++) {
        // 从上往下
        result[i] = result[i-1] * A[i-1];
    }

    int temp = 1;

    for (int j = A.size()-2; j >= 0; j--) {
        // 从下往上
        temp *= A[j+1];
        result[j] *= temp;
    }

    return result;
}