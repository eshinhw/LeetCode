
public class SearchInsertPosition {
	
    public int searchInsert(int[] nums, int target) {
    	
    	for (int i=0; i < nums.length; i++) {
    		
    		if (target < nums[0])
    			return 0;
    		else if ((nums[i] == target) || (target < nums[i]))
    			return i;
    		else if (nums[nums.length-1] < target)
    			return nums.length;
    	}
    	
    	return 0;
        
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		SearchInsertPosition sip = new SearchInsertPosition();
		
		int[] test = {1,3,5,6};
		
		int output1 = sip.searchInsert(test, 5);
		int output2 = sip.searchInsert(test, 2);
		int output3 = sip.searchInsert(test, 7);
		int output4 = sip.searchInsert(test, 0);
		
		System.out.println(output1);
		System.out.println(output2);
		System.out.println(output3);
		System.out.println(output4);
		
		

	}

}
