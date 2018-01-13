
/*
371. Sum of Two Integers
DescriptionHintsSubmissionsDiscussSolution
DiscussPick One
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

Credits:
Special thanks to @fujiaozhu for adding this problem and creating all test cases.

*/


//直接a+b 也能过？？...

//大神一句话 借用欧几里得+位运算？？？
class Solution {
    public int getSum(int a, int b) {
          return b == 0 ? a : getSum(a ^ b, (a & b) << 1);
    }
}