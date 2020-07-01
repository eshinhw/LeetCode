
public class RemoveDuplicatesFromSortedArray {

    public int removeDuplicates(int[] nums) {
    	
    	int duplicatesCount = 0;
    	
    	
    	
    	for (int i=1; i < nums.length; i++) {
    		
    		if (nums[i] != nums[i-1] && i != nums.length) {
    			duplicatesCount++;
    		}
    	}
    	
    	int validIdx = duplicatesCount;
    	int offIdx = validIdx + 1;
    	
    	for (int i=0; i < duplicatesCount; i++) {
    		if (nums[i] != nums[i+1])
    			continue;
    		
    	}
    	
    	System.out.println(duplicatesCount);
    	
    	return 0;        
    }
	
	
	public static void main(String[] args) {

		RemoveDuplicatesFromSortedArray rdfsa = new RemoveDuplicatesFromSortedArray();
		
		int[] test1 = {1,1,2};
		int[] test2 = {0,0,1,1,1,2,2,3,3,4};
		
		rdfsa.removeDuplicates(test1);
		

	}

}
