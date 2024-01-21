# 3017. Count the Number of Houses at a Certain Distance II.

"""
### Task:
---------
You are given three positive integers n, x, and y.

In a city, there exist houses numbered 1 to n connected by n streets. There is a street connecting the house numbered i with the house numbered i + 1 for all 1 <= i <= n - 1 . An additional street connects the house numbered x with the house numbered y.

For each k, such that 1 <= k <= n, you need to find the number of pairs of houses (house1, house2) such that the minimum number of streets that need to be traveled to reach house2 from house1 is k.

Return a 1-indexed array result of length n where result[k] represents the total number of pairs of houses such that the minimum streets required to reach one house from the other is k.

Note that x and y can be equal.




Example 1:

Input: n = 3, x = 1, y = 3
Output: [6,0,0]
Explanation: Let's look at each pair of houses:
- For the pair (1, 2), we can go from house 1 to house 2 directly.
- For the pair (2, 1), we can go from house 2 to house 1 directly.
- For the pair (1, 3), we can go from house 1 to house 3 directly.
- For the pair (3, 1), we can go from house 3 to house 1 directly.
- For the pair (2, 3), we can go from house 2 to house 3 directly.
- For the pair (3, 2), we can go from house 3 to house 2 directly.

Example 2:

Input: n = 5, x = 2, y = 4
Output: [10,8,2,0,0]
Explanation: For each distance k the pairs are:
- For k == 1, the pairs are (1, 2), (2, 1), (2, 3), (3, 2), (2, 4), (4, 2), (3, 4), (4, 3), (4, 5), and (5, 4).
- For k == 2, the pairs are (1, 3), (3, 1), (1, 4), (4, 1), (2, 5), (5, 2), (3, 5), and (5, 3).
- For k == 3, the pairs are (1, 5), and (5, 1).
- For k == 4 and k == 5, there are no pairs.

Example 3:

Input: n = 4, x = 1, y = 1
Output: [6,4,2,0]
Explanation: For each distance k the pairs are:
- For k == 1, the pairs are (1, 2), (2, 1), (2, 3), (3, 2), (3, 4), and (4, 3).
- For k == 2, the pairs are (1, 3), (3, 1), (2, 4), and (4, 2).
- For k == 3, the pairs are (1, 4), and (4, 1).
- For k == 4, there are no pairs.

 
Constraints:

    2 <= n <= 105
    1 <= x, y <= n

"""
### Solution Python:

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x > y: x, y = y, x
        ans = [0] * (n + 2)
        x -= 1
        y -= 1
        for i in range(n):
            l, r = i + 1, n - 1
            while l <= r:
                m = (l + r) // 2
                if m - i < abs(i - x) + abs(m - y) + 1:
                    l = m + 1
                else:
                    r = m - 1
            ans[1] += 1
            ans[r+1-i] -= 1
            
            if l == n: continue
            end = y
            val = abs(i - x) + 1
            if l < y:
                # val + 1, val + 2, ..., val + y - l
                ans[val + 1] += 1
                ans[val + y - l + 1] -= 1
            
            # val, val + 1, ..., val + n - 1 - y
            ans[val] += 1
            ans[val + n - y] -= 1
        ans = list(accumulate(ans))
        return [x * 2 for x in ans[1:-1]]







### Solution Java:
'''
class Solution {
    public long[] countOfPairs(int n, int x, int y) {
        if (x > y) {
            int t = x;
            x = y;
            y = t;
        }
        long[] ans = new long[n];
        long[] diff = new long[n + 2];
        for (int i = 1; i <= n; i++) {
            ans[i - 1] += (n - i) * 2;
            if (x == y || x == y - 1) {
                continue;
            }
            long max = (long)Math.min(x - 1, i - 1);
            long min = (long)Math.max(0, (i - 1 - (n - y)));
            if (max >= min) {
                ans[i - 1] += (max - min + 1L) * 2L;
                if (i + (y - x - 1) <= n - 1) {
                    ans[i + (y - x - 1) - 1] -= (max - min + 1L) * 2L;
                }
            }
            
            max = (long)Math.min(x - 1, i - 2);
            min = (long)Math.max(0, i - 1 - (y - (y + x + 1) / 2 - 1));
            if (max >= min) {
                ans[i - 1] += (max - min + 1L) * 2L;
                int start = y - (i - 1 - (int)min) - (x - (int)min);
                int end = y - (i - 1 - (int)max) - (x - (int)max);
                diff[start - 1] -= 2L;
                diff[end + 1] += 2L;
            }
            max = (long)Math.min(n - y, i - 2);
            min = (long)Math.max(0, i - 1 - ((y + x - 2) / 2 - x));
            if (max >= min) {
                ans[i - 1] += (max - min + 1L) * 2L;
                int start = y + (int)min - (x + (i - 1 - (int)min));
                int end = y + (int)max - (x + (i - 1 - (int)max));
                diff[start - 1] -= 2L;
                diff[end + 1] += 2L;
            }
            if (2 * i < y - x + 1) {
                ans[i - 1] += (long)Math.max(0, i - 2) * 2L;
                ans[(y - x + 1 - i) - 1] -= (long)Math.max(0, i - 2) * 2L;
            }
        }
        for (int i = 0; i < n; i++) {
            diff[i] += i >= 2 ? diff[i - 2] : 0L;
            ans[i] += diff[i];
        }
        return ans;
    }
}

'''




### Solution C
"""
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* countOfPairs(int n, int x, int y, int* returnSize) {
    
}

-------------------------------------------------------

class Solution {
public:
    vector<long long> countOfPairs(int n, int x, int y) {
        vector<long long>psa(n+5);
        if(x > y)swap(x,y);
        if(x==y){
            for(int i = 1; i<=n; i++){
                psa[1]++; psa[i]--;
                psa[1]++;
                psa[n+1-i]--;
            }
        }
        else{
            for(int i = 1; i<=n; i++){
                if(i<=x){
                    psa[1]++; psa[i]--; // [0 to i)
                    psa[1]++; psa[x-i+1]--; // (i to x]
                    int rq = y-x;
                    int v = rq/2;
                    int v2 = rq-v;
                    psa[x-i+1]++; psa[v+1+x-i]--;
                    psa[x-i+1]++; psa[v2+1+x-i]--;
                    // (x to y]
                    psa[x-i+2]++; psa[n+1-y+1+x-i]--; // (y to n]
                }
                else if(i>=y){
                    psa[1]++; psa[n-i+1]--;
                    psa[1]++; psa[i-y+1]--; // [y to i)

                    int rq = y-x;
                    int v = rq/2;
                    int v2 = rq-v;
                    psa[i-y+1]++; psa[i-y+v+1]--;
                    psa[i-y+1]++; psa[i-y+v2+1]--;

                    psa[i-y+2]++; psa[x+1+i-y]--;
                    // [1 , x)

                }
                else{
                    int rq = y-x;
                    int v = rq/2;
                    int v2 = rq-v;
                    psa[1]++; psa[v+1]--;
                    psa[1]++; psa[v2+1]--;
                    int dx = min(i-x,y-i+1);
                    int dy = min(y-i,i-x+1);
                    psa[dx+1]++;
                    psa[dx+x]--;
                    psa[dy+1]++;
                    psa[dy+n-y+1]--;
                }
            }
        }
        
        vector<long long>ans;
        for(int i = 1; i<=n; i++){
            psa[i]+=psa[i-1];
            ans.push_back(psa[i]);
        }
        return ans;
    }
};


"""
