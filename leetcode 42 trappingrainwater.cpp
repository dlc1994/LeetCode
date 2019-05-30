// hard
// 维护最短的一边，另一道两块板装水最多的同理
class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size()<=1){return 0;}
        int n = height.size();
        int left = 0, right = n-1;
        int maxLeft = 0, maxRight=0;
        int res = 0;
        while(left<right){
            if(height[left]<=height[right]){
                if(height[left]>=maxLeft) maxLeft=height[left];
                else res += maxLeft - height[left];
                left++;
            }
            else{
                if(height[right]>=maxRight) maxRight=height[right];
                else res+=maxRight - height[right];
                right--;
            }
        }
        return res;
    }
};
