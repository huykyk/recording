/**
*

136. Single Number
DescriptionHintsSubmissionsDiscussSolution
DiscussPick One
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
*/

//神仙算法：异或
class Solution {
    public int singleNumber(int[] nums) {
        int res = 0;
        for(int i=0;i<nums.length;i++) res ^= nums[i];
        return res;
    }
}