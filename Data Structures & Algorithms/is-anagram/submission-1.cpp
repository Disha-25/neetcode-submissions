class Solution {
public:
    bool isAnagram(string s, string t) {
        // sorting - O(nlogn +mlogm), O(n+m)/O(1)
        // if(s.length() != t.length())
        // return false;
        // sort(s.begin(), s.end());
        // sort(t.begin(), t.end());
        // s == t ? true : false;

        // Hash map - O(n + m), O(1)
        // unordered_map<char,int> smap;
        // unordered_map<char,int> tmap;
        // for (int i=0, i < s.length(), i++) {
        //     smap[s[i]]++;
        //     tmap[t[i]]++;
        // }
        // return smap == tmap;

        // Hash Table
        if(s.length() != t.length()) {
            return false;
        }
        vector<int> arr(26,0);
        for(int i=0; i<s.length(); i++) {
            arr[s[i]-'a']++;
            arr[t[i]-'a']--;
        }
        for (int n: arr) {
            if (n!= 0) return false;
        }
        return true;
    }
};
