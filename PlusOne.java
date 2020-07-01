
public class PlusOne {
	
    public int[] plusOne(int[] digits) {
    	
    	// If the last digit of a given array is 9, we need one more space 
    	
    	if (digits[digits.length-1] == 9) {
    		
    		int[] copy1 = new int[digits.length+1];
    		
    		for (int i=0; i < digits.length+1; i++) {
    			
    			if (i == digits.length-1) {
    				copy1[i] = 1;
    				copy1[i+1] = 0;
    				break;
    			} else {
    				copy1[i] = digits[i];
    			}
    		}
    		
    		return copy1;
    	} 
    	
    	// If the last digit of a given array is not 9, we can simple add 1 to the last element
    	
    	else {
    		
        	int[] copy2 = new int[digits.length];
        	
        	for (int i=0; i < digits.length; i++) {
        		if (i == digits.length-1)
        			copy2[i] = digits[i]+1;
        		else
        			copy2[i] = digits[i];
        	}
        	
        	return copy2;
    		
    	}
    	
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		PlusOne po = new PlusOne();
		
		int[] test = {1,2,9};
		int[] test2 = {4,3,2,1};
		
		int[] output = po.plusOne(test);
		int[] output2 = po.plusOne(test2);
		
		for (int i : output)
			System.out.println(i);
		
		for (int i : output2)
			System.out.println(i);

	}

}
