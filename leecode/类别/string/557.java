
/*
557. Reverse Words in a String III
DescriptionHintsSubmissionsDiscussSolution
DiscussPick One
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.

*/
class Solution {
    public String reverseWords(String s) {
        String[] tokens = s.split(" ");
        
        for(int i=0;i<tokens.length;i++){
           tokens[i] = new StringBuilder(tokens[i]).reverse().toString();//not bufferbuilder
        }
        StringBuilder res = new StringBuilder();
        for(String token:tokens)
            res.append(token+" ");
        return res.toString().trim();

    }
}