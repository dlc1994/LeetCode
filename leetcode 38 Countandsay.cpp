class Solution {
public:
    string countAndSay(int n) {
        int cnt = 1;
        string res = "1";
        while(cnt<n){
            int count = 1;
            for(int i=0;i<res.size();i++){
                while((i+1)<res.size() && res[i]==res[i+1]){
                    count++;
                    i++;
                }
                res += to_string(count)+res[i];
            }
            cnt++;
        }
        return res;
    }
};
