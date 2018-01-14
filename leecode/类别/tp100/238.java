/**
*

238. Product of Array Except Self
DescriptionHintsSubmissionsDiscussSolution
DiscussPick One
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)


*/
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        int left = 1;
        for(int i=0;i<n;i++){
            if(i>0){ left = left * nums[i-1];}
            res[i]=left;
        }
        int right =1;
        for(int i=n-1;i>=0;i--){
            if(i<n-1){ right= right * nums[i+1]; }
            res[i]*=right;
        }
        return res;
        
    }
}