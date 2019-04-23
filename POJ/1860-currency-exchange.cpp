#include <cstdio>
#include <cstring>

int n, m, s, C;
double v, dis[110];

struct Edge
{
    int a, b;
    double rate, cost;
}edge[500];

bool bellman_ford()
{
    memset(dis, 0, sizeof(dis));  //此处与Bellman-Ford的处理相反，初始化为源点到各点距离0，到自身的值为原值
    dis[s] = v;
    for(int i = 1; i <= n; i++)
    {
        bool flag = false;
        for(int j = 0; j < C; j++)
        {
            int a = edge[j].a, b = edge[j].b;
            double rate = edge[j].rate, cost = edge[j].cost;
            if(dis[b] < (dis[a] - cost) * rate)
            {
                 dis[b] = (dis[a] - cost) * rate;
                 flag = true;
            }

        }
        if(!flag)
            break;
    }
    for(int i = 0; i < C; i++)
        if(dis[edge[i].b] < (dis[edge[i].a] - edge[i].cost) * edge[i].rate)    //正环能够无限松弛
            return true;
    return false;
}

int main()
{
    int i, j, a, b;
    double rab, rba, cab, cba;
    while(~scanf("%d%d%d%lf",&n,&m,&s,&v))
    {
        C = 0;
        for(i = 0; i < m; i++)
        {
            scanf("%d%d%lf%lf%lf%lf",&a, &b, &rab, &cab, &rba, &cba);
            edge[C].a = a;
            edge[C].b = b;
            edge[C].rate = rab;
            edge[C++].cost = cab;
            edge[C].a = b;
            edge[C].b = a;
            edge[C].rate = rba;
            edge[C++].cost = cba;
        }
        if(bellman_ford())
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}