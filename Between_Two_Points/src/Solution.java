import java.util.Arrays;

public class Solution {

    public int maxWidthOfVerticalArea(int[][] points) {
        int max_ = -999;
        Arrays.sort(points, (a,b)->Integer.compare(a[0],b[0]));
        for(int i =1;i<points.length;i++){
            max_ = Math.max(max_,points[i][0]-points[i-1][0]);
        }
        return max_;
    }

}
