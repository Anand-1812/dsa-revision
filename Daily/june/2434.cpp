#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string robotWithString(string s) {
      int n = s.length();
      
      // preprocessing the min character :-
      vector<char> minCharToRight(n);
      minCharToRight[n-1] = s[n-1];
      for (int i = n-2;i >= 0;i--) {
        minCharToRight[i] = min(s[i], minCharToRight[i+1]);
      }

      string t = "";
      string result;
      int i = 0;
      while (i < n) {
        t.push_back(s[i]);
        char minChar = (i+1 < n) ? minCharToRight[i+1] : s[i];

        // pop from t and push to result;
        while (!t.empty() && t.back() <= minChar) {
          result += t.back();
          t.pop_back();
        }
        i++;
      }

      // Filling remianing elements
      while (!t.empty()) {
        result += t.back();
        t.pop_back();
      }

      return result;
    }
};
