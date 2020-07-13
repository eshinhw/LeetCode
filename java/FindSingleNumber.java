import java.util.*;


public class FindSingleNumber {
	
	public void swap (int[] arr, int indexMin, int i) {
		int temp = arr[i];
		arr[i] = arr[indexMin];
		arr[indexMin] = temp;
	}
	
	public void selectionSortV1 (int[] arr) {
		int indexMin;
		
		for (int i=0; i < arr.length-1; i++) {
			indexMin = i;
			
			for (int j=i+1; j < arr.length; j++) {
				if (arr[i] < arr[indexMin])
					indexMin = j;
			}	
			swap (arr, indexMin, i);
		}		
		
	}
	
	public int singleNumber (int[] nums) {
		
		
		
		selectionSortV1(nums);
		
		for (int v : nums)
			System.out.println(v);
		
//		for (int i=1; i < nums.length; i++) {
//			if (nums[i-1] < nums[i] && nums[i] < nums[i+1])
//				
//		}
		
		return 0;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		FindSingleNumber sn = new FindSingleNumber();
		
		int[] test = {4,1,2,1,2};
		
		int output = sn.singleNumber(test);
		System.out.println(output);

	}

}
