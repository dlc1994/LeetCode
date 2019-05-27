//leetcode 38 easy
class Solution {
public:
    string countAndSay(int n) {
        int cnt = 1;
        string res = "1";
        while(cnt<n){
            string result = "";
            for(int i=0;i<res.size();i++){
                int count = 1;
                while((i+1)<res.size() && res[i]==res[i+1]){
                    count++;
                    i++;
                }
                result += to_string(count)+res[i];
            }
            cnt++;
            res = result;
            cout<<cnt<<" "<<res<<endl;
        }
        return res;
    }
};

