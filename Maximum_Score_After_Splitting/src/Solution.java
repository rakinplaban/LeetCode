import java.lang.String;
public class Solution {
    public int maxScore(String s) {
        int j = 0,k=1;
        int count0 = 0, count1 = 0,max_ = -999;
        for(int i=0;i < s.length();i++){
            if(s.charAt(j) == '0'){
                count0++;
                j++;
            }

            if(k<s.length()){
                for(int l=k;l<s.length();l++){
                    if(s.charAt(l)=='1'){
                        count1++;
                    }
                }
                k++;
            }
            max_ = Math.max(max_,count0+count1);
            // count0 = 0;
            count1=0;
        }
        return max_;
    }
}
