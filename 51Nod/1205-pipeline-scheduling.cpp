// 机器调度问题，这是一个经典问题: 2台机器的情况下有多项式算法（Johnson算法），3台或以上的机器是NP-hard算法。

#include <cstdio>
#include <algorithm>

typedef struct TASK {
    int a; // 在 M1机器上加工需要的时间
    int b; // 在 M2机器上加工需要的时间
};

// 把作业按工序加工时间分成两个子集
TASK taskA[50001]; // 第一个集合中在M1上做的时间比在M2上少
TASK taskB[50001]; // 其它的作业放到第二个集合
// 先完成第一个集合里面的作业，再完成第二个集合里的作业

bool cmpA(TASK a, TASK b) {
    return a.a <= b.a;
}

bool cmpB(TASK a, TASK b) {
    return a.b >= b.b;
}

int main(int argc, char *argv[]) {
    int N;
    scanf("%d", &N);

    int a, b;
    int posA = 0, posB = 0;
    int sumA = 0, sumB = 0;

    for (int i = 0; i < N; i++) {
        scanf("%d%d", &a, &b);

        if (a < b) {
            taskA[posA].a = a;
            taskA[posA++].b = b;
            sumA += b;
        } else {
            taskB[posB].a = a;
            taskB[posB++].b = b;
            sumB += a;
        }
    }

    // 对于第一个集合，其中的作业顺序是按在M1上的时间的不减排列
    // 因为对于第一个集合满足a < b，如果对于a是递增的，那么 task[i].a + task[i+1].a 和task[i].a + task[i].b的绝对差会小
    std::sort(taskA, taskA+posA, cmpA);
    // 对于第二个集合, 其中的作业顺序是按在M2上的时间的不增排列
    // 因为对于第二个集合满足a >= b，如果对于b是递减的，那么 task[i].a + task[i+1].a 和task[i].a + task[i].b的绝对差会小
    std::sort(taskB, taskB+posB, cmpB);

    for (int i = 0; i < posB; i++) {
        taskA[posA++] = taskB[i];
    }

    int ans = taskA[0].a + taskA[0].b;
    int sum = taskA[0].a;

    for (int i = 1; i < posA; i++) {
        sum += taskA[i].a;
        // 思想：task[i+1].a 进行时 task[i].b 也可以同时进行
        // 比如先用 M1 机器耗时 task[i].a 完成 task[i] 的一部分
        // 再用 M1 机器耗时 task[i+1].a 完成 task[i+1] 的一部分 以及 用 M2 机器耗时 task[i].b 完成 task[i] 的最后一部分
        // 那么就比较 task[i].a + task[i+1].a 和 task[i].a + task[i].b 谁花的时间长
        ans = sum < ans ? ans + taskA[i].b : sum + taskA[i].b;
    }

    printf("%d\n", ans);

    return 0;
}
