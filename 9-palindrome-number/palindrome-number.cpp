class Solution {
public:
    bool isPalindrome(int x) {

        if(x < 0 || (x % 10 == 0 && x != 0))
            return false;

        int revnum = 0;

        while(x > revnum) {
            int ld = x % 10;
            revnum = revnum * 10 + ld;
            x = x / 10;
        }

        return x == revnum || x == revnum / 10;
    }
};