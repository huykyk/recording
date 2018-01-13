class Solution {
    public String reverseString(String s) {
        
        return new StringBuffer(s).reverse().toString();
        
        
        
        // String result = ""; //not ''
        // char[] ch = s.toCharArray();
        // for(int i=ch.length-1;i>=0;i--){
        //     result += ch[i];
        // }
        // return result;
    }
}