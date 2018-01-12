class Solution {
public:
    bool checkRecord(string s) {
        int a{0};
        int l{0};
        for(char c:s){
            if(c=='A') a++;
            if(c=='L') l++;
            else l=0;
            if(a>1 || l>2)  return false;     
        }
        return true;
       // or 正则 //return !std::regex_search(s,std::regex("A.*A|LLL"));
    }
};

