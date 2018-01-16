/*
537. Complex Number Multiplication
DescriptionHintsSubmissionsDiscussSolution
DiscussPick One
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.
*/

class Solution {
    public String complexNumberMultiply(String a, String b) {
        
        // a b c d
        String[] tokena = a.split("[+i]");
        int aa = Integer.parseInt(tokena[0]);
        int bb = Integer.parseInt(tokena[1]);
        
        String[] tokenb = b.split("[+i]");
        int c = Integer.parseInt(tokenb[0]);
        int d = Integer.parseInt(tokenb[1]);
        
        
        return aa*c-bb*d +"+"+ (aa*d+bb*c) +"i" ;
    }
}