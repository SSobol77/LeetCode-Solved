# 3015. Count the Number of Houses at a Certain Distance I.

"""
### Task:
--------
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
2 <= n <= 100
1 <= x, y <= n


"""
### Solution:

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        result = [0] * n

        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                direct_dist = j - i
                via_xy_dist = min(abs(x - i), abs(y - i)) + 1 + min(abs(x - j), abs(y - j))
                min_dist = min(direct_dist, via_xy_dist)
                result[min_dist - 1] += 2

        return result

# ----------------------------------------------
# Solution Java:
'''
class Solution {

	public int[] countOfPairs(int n, int x, int y) {
		if (x > y) {
			return countOfPairs(n, y, x);
		}
		int[] count = new int[n];
		for (int i = 1; i < n; i++) {
			count[Math.min(i, Math.abs(y - i - 1) + x) - Math.min(i, x)] += 2;
			count[Math.min(i, Math.abs(y - i - 1) + x)] -= 2;
			if (x < i) {
				count[0] += 2;
				count[i - Math.max(x, (x + i - Math.abs(y - i - 1) - 1) / 2)] -= 2;
				if (x + i > Math.abs(y - i - 1) + 2) {
					count[Math.abs(y - i - 1) + 1] += 2;
					count[Math.abs(y - i - 1) + 1 + Math.max(0, (x + i - Math.abs(y - i - 1) - 1) / 2 - x)] -= 2;
				}
			}
		}
		for (int i = 1; i < n; i++) {
			count[i] += count[i - 1];
		}
		return count;
	}
}

'''

# ----------------------------------------------
# Solution C:
'''
class Solution {
public:
    vector<int> countOfPairs(int n, int x, int y) {
        vector<int>psa(n+5);
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
        
        vector<int>ans;
        for(int i = 1; i<=n; i++){
            psa[i]+=psa[i-1];
            ans.push_back(psa[i]);
        }
        return ans;
    }
};



'''
