#include<bits/stdc++.h>
using namespace std;

#define FIO ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
#define int long long
#define endl '\n'



void solve(){
    int n, d;
    cin>>n>>d;
    int a[n];
    vector<int> cnt(1000001);
    for(int i = 0; i<n; i++){
        cin>>a[i];
    }
    for(int i = 0; i<n; i++){
        cnt[a[i]] = 0;
    }
    //Design a window/ snake
    int head = 0, tail = 0;
    int cntr = 0;
    int distinct = 0;
    int ans = 1000000001;

    // Main two pointers

    for(int i = 0; i<d; i++){
        if(cnt[a[i]] == 0){
            distinct++;
        }
        cnt[a[i]]++;
    }
    ans = distinct;
    for(int i = 0; i< n-d; i++){
        cnt[a[i]]--;
        if(cnt[a[i]] == 0){
            distinct--;
        }
        if(cnt[a[i+d]] == 0){
            distinct++;
        }
        cnt[a[i+d]]++;
        ans = min(ans, distinct);
    }
    cout<<ans<<endl;
    return;
}


signed main(){
    FIO
    int t = 1;
    cin>>t;
    while(t--){
        solve();
    }
    return 0;
}