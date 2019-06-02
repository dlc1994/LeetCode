#medium
class Solution {
public:

    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        while(matrix.size()>0){
            for(int i=0;i<matrix[0].size();i++){
                res.push_back(matrix[0][i]);
            }
            matrix.erase(matrix.begin());
            matrix = rotate(matrix);
        }
        return res;
    }
    vector<vector<int>> rotate(vector<vector<int>>& matrix) {
        if (matrix.size() == 0) return matrix;
        vector<vector<int>> v;
        int nrows = matrix.size(), ncols = matrix[0].size();
        for (int i = 0; i < ncols; i++) {
            vector<int> tmp;
            for (int j = 0; j < nrows; j++) {
                tmp.push_back(matrix[j][i]);
            }
            v.push_back(tmp);
        }
        reverse(v.begin(), v.end());
        return v;
    }
};
