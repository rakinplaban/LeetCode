public class Solution {
    public int minOperations(String s) {
        int start_0 = 0, start_1 = 0;
        for(int i=0;i<s.length();i++){
            if(i%2==0){
                if (s.charAt(i)=='0'){
                    start_0++;
                }else {
                    start_1++;
                }
            }else{
                if(s.charAt(i)=='1'){
                    start_0++;
                }else{
                    start_1++;
                }
            }
        }
        return Math.min(start_0,start_1);
    }
}
