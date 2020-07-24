import java.util.*;


public class TwoSums {

    public int[] twoSum (int[] nums, int target) {
    	
    	int[] output = new int[2];    	
    	
        for (int i=0; i < nums.length; i++) {
        	for (int j=i+1; j < nums.length; j++) {
        		if (nums[i] + nums[j] == target) {
        			output[0] = i;
        			output[1] = j;
        			return output;
        		}
        	}
        }
        return output;        
    }
    
    public int[] twoSumHashMap (int[] nums, int target) {
    	
    	if (nums.length < 2)
    		return null;
    	
    	HashMap<Integer,Integer> count = new HashMap<>();
    	
    	for (int i=0; i < nums.length; i++) {
    		if (count.containsKey(target - nums[i]))
    			return new int[] {i,count.get(target-nums[i])};
    		else
    			count.put(nums[i], i);    			
    	}
    	
    	return null;
    }
    	
    	
    	

}

