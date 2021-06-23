
import java.util.*;

public class MajorityElement {
	
    public int majorityElement(int[] nums) {
    	
    	int threshold = nums.length/2;
    	int majority = 0;
    	
    	HashMap<Integer,Integer> count = new HashMap<Integer,Integer>();
    	
    	for (int i=0; i < nums.length; i++) {
    		
    		if (count.containsKey(nums[i])) {
    			int val = count.get(nums[i]);
    			count.put(nums[i], val+1);
    		} else {
    			count.put(nums[i],1);
    		}    		
    	}
    	
    	for (Map.Entry<Integer,Integer> entry : count.entrySet()) {
    		if (entry.getValue() > threshold) {
    			majority = entry.getKey();
    		}
    	}
    		
    	
    	return majority;
        
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		int[] test1 = {3,2,3};
		int[] test2 = {2,2,1,1,1,2,2};
		
		MajorityElement me = new MajorityElement();
		System.out.println(me.majorityElement(test1));
	}

}
