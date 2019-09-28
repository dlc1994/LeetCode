// cpp
int longestConsecutive(vector<int> &num) {
    unordered_map<int, int> m;
    int r = 0;
    for (int i : num) {
        if (m[i]) continue;
        r = max(r, m[i] = m[i + m[i + 1]] = m[i - m[i - 1]] = m[i + 1] + m[i - 1] + 1);
    }
    return r;
}
int longestConsecutive(vector<int>& nums) {
    if (nums.size() == 0) return 0;
    unordered_map<int, int> map;
    int best = 0;
    for (int i : nums) {
        if (map[i]) continue;
        else if (map[i+1] == 0 && map[i-1] == 0) {
            map[i] = 1;
        }
        else if (map[i+1] == 0 && map[i-1] != 0) {
            map[i] = map[i-map[i-1]] = map[i-1] + 1;
        }
        else if (map[i+1] != 0 && map[i-1] == 0) {
            map[i] = map[i+map[i+1]] = map[i+1] + 1;
        }
        else if (map[i+1] != 0 && map[i-1] != 0) {
            map[i] = map[i+map[i+1]] = map[i-map[i-1]] = map[i+1] + map[i-1] +1;
        }
        best = max(best, map[i]);
    }
    return best;
}

//python
def longestConsecutive(self, nums):
    nums = set(nums)
    best = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)
    return best
