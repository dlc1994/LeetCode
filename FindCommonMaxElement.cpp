// 找出两个数组中的公共最大元素
    int findCommonMax1(vector<int> &a, vector<int> &b){ //O(n*m)
        int max_ = 0;
        for(int i=0;i<a.size();i++){
            for(int j=0;j<b.size();j++){
                if(b[j]==a[i]){
                    if(b[j]>max_) max_ = b[j];
                }
            }
        }
        return max_;
    }
    int findCommonMax2(vector<int> &a, vector<int> &b){ //O(max(n, m))
        int max_ = 0;
        unordered_map<int, int> mp;
        for(int i=0;i<a.size();i++){
            mp[a[i]]++;
        }
        for(int j=0;j<b.size();j++){
            mp[b[j]]++;
        }
        for(auto i=mp.begin();i!=mp.end();i++){
            if(i->second>=2){
                if(i->first>max_) max_=i->first;
            }
        }
        return max_;
    }
