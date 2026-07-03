class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // [1, 2, 3, 3]
        // Sorting - O(nlogn), O(1)/O(n)
        // sort(nums.begin(), nums.end());
        // int n = nums.size();
        // for(int i=1; i<n; i++){
        //     if(nums[i] == nums[i-1]){
        //         return true;
        //     }
        // }
        // return false;

        // Hash Set - O(n), O(n)
        // unordered_set<int> s;
        // for (int num: nums) {
        //     if(s.count(num)) {
        //         return true;
        //     }
        //     s.insert(num);
        // }
        // return false;

        // Hash Set length - 
        return unordered_set<int>(nums.begin(),nums.end()).size() < nums.size();

    }
};
