//hard

#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) { //O(n)复杂度有待考证
        int n = nums.size();
        for (int i = 0; i < n; i++)
            while (nums[i] > 0 && nums[i] <= n && nums[nums[i] - 1] != nums[i])
                swap(nums[i], nums[nums[i] - 1]);
        for (int i = 0; i < n; i++)
            if (nums[i] != i + 1)
                return i + 1;
        return n + 1;
    }
    int first(vector<int>& nums){
        nums.push_back(0);
        int n = nums.size();
        for(int i=0;i<n;++i){
            if(nums[i]<0 || nums[i]>n){
                nums[i]=0;
            }
        }
        for(int i=0;i<n;++i){
            nums[nums[i]%n]+=n; //每个位置存原来的数及频率
        }
        for(int i=0;i<n;++i){
            if(nums[i]/n==0) //能被n整除说明该下标没有数
                return i;
        }
        return n;
    }
    void swap(int& m, int& n){
        int tmp = m;
        m = n;
        n = tmp;
    }
};
int main() {
    Solution s;
    vector<int> alist = {3,4,-1,1};
    cout<<s.first(alist)<<endl;
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
