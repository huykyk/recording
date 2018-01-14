/**
*
171. Excel Sheet Column Number
DescriptionHintsSubmissionsDiscussSolution
DiscussPick One
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
Credits:
Special thanks to @ts for adding this problem and creating all test cases.

*/
class Solution {
    public int titleToNumber(String s) {
        int res = 0;
        for(int i=0;i<s.length();i++){
            res = res*26 + s.charAt(i) - 'A' +1;
        }
        return res;
    }
}