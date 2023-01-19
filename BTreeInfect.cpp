#include <bits/stdc++.h>
using namespace std;
int main()
{
    int V;
    cout<<"Number of vertices:";
    cin>>V;
    int E;
    cout<<"Number of Edges:";
    cin>>E;
    pair<int,int> tmp;
    cout<<"Enter element to be searched:";
    int X;cin>>X;
    int graph[V][V];
    for (size_t i = 0; i < V; i++)
        for (size_t j = 0; j < V; j++)
            graph[i][j]=0;
    cout<<"Enter Edges:\n";
    for (int i = 0; i < E; i++)
    {
        cin>>tmp.first>>tmp.second;
        graph[tmp.first][tmp.second]=1;
        graph[tmp.second][tmp.first]=1;
    }
    deque<int> q1;
    q1.push_back(X);
    unordered_map<int,int> m1;
    while (q1.size())
    {
        int curre = q1.at(0);
        q1.pop_front();
        for (size_t j = 0; j < V; j++)
        {
            if(graph[curre][j])
            {
                q1.push_back(j);
                graph[curre][j]=0,graph[j][curre]=0;
                m1[j] = m1[curre]+1;
            }
        }  
    }
    int maxxlevel = 0;
    for(auto iter = m1.begin();iter!=m1.end();iter++)
    {
        maxxlevel = max(maxxlevel,iter->second);
    }
    printf("%d seconds will be taken to infect the whole tree\n",maxxlevel);
}
