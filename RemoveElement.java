
public class RemoveElement {
	
	public int removeElement (int[] nums, int val) {
		
		int size = nums.length;
		
		// Determine the new length after removing the parameter val 
			
		for (int i=0; i < nums.length; i++) {
			if (nums[i] == val)
				size--;
		}		
		
		int offIdx = size;
		
		for (int i=0; i < size; i++) {
			if (nums[i] == val) {
				// Swap the elements since we have the matching element within the new length
				
				// Find the non-matching element doing while loop
				// If nums[offIdx] == val, we need to go to the next element until we find the non-matching element for swap
				while (nums[offIdx] == val)
					offIdx++;
				
				// Since we find the non-matching element, we swap nums[offIdx] with nums[i]
				int temp = nums[offIdx];				
				nums[offIdx] = nums[i];
				nums[i] = temp;				
			}
		}
				
		return size;
	}
	
	public static void main (String[] args) {
		RemoveElement re = new RemoveElement();
		
		int[] nums = {3,2,2,3};
		int val = 3;
		
		int output = re.removeElement(nums, val);
		
		System.out.println("Output: " + output);
		
		for (int i=0; i<output; i++)
			System.out.println(nums[i]);
		
		
	}

}
