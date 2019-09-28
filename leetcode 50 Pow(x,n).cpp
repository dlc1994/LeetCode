// Implement pow(x, n), which calculates x raised to the power n (x^n).
// Medium

// error stack-overflow
double myPow(double x, int n) {
    if (n == 0) return 1;
    if (n > 0) return x * myPow(x, n - 1);
    else return 1 / x * myPow(x, n + 1);
}

// TLE
double myPow(double x, int n) {
    int flag = 1;
    if (n == 0) return 1;
    if (n < 0) flag = 0;
    n = abs(n);
    double res = 1;
    while (n--) {
        res *= x;
    }
    if (flag) return res;
    else return 1 / res;
}

double myPow(double x, int n) {
    int flag = 1;
    if (n == 0) return 1;
    if (x == 1) return 1;
    if (x == -1) {
        if (n % 2 == 0) return 1;
        else return -1;
    }
    if (n < 0) flag = 0;
    if (n == INT_MIN) {
        return 0;
    }
    n = abs(n);
    double res = 1;
    while (n > 0) {
        if (n & 1) {
            res *= x;
        }
        x *= x;
        n = n >> 1;
    }
    if (flag) return res;
    else return 1 / res;
}
