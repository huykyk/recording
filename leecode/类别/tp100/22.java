/*
22. Generate Parentheses
DescriptionHintsSubmissionsDiscussSolution
DiscussPick One
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
*/
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<String>();
        if(n>0) genereParenthesisFirst("",n,n,res);
        return res; 
    }
        private void genereParenthesisFirst(String pre,int left,int right,List<String> res)
        {
            if(left==0&&right==0) res.add(pre);
            if(left>0) genereParenthesisFirst(pre+'(',left-1,right,res);
            if(left<right) genereParenthesisFirst(pre+')',left,right-1,res);
        }
   
}
