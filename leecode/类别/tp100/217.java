/*
217. Contains Duplicate
DescriptionHintsSubmissionsDiscussSolution
DiscussPick One
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Seen this question in a real interview before?  YesNo

*/

class Solution {
    public boolean containsDuplicate(int[] nums) {
      Arrays.sort(nums);
        for(int i=1;i<nums.length;i++){
            if(nums[i]==nums[i-1]) return true;
        }
        return false;
   }
}
class Solution {
    public boolean containsDuplicate(int[] nums) {
     Set<Integer> set = new HashSet<Integer>();//Set 
        for(int i:nums)
            if(!set.add(i)) return true;
        return false;
   }
}