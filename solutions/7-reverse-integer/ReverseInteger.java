
public class ReverseInteger {
	
	public int reverse (int x) {
		
		long reversed = 0;
		
		System.out.println("Input: " + x);
					
		while(x != 0) {	    	 
			reversed = reversed * 10 + x % 10;
			x = x / 10;
		}
		
		if (reversed > Integer.MAX_VALUE || reversed < Integer.MIN_VALUE)
			return 0;
		else
			return (int)reversed;
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		ReverseInteger ri = new ReverseInteger();
		
		int output = ri.reverse(1534236469);


	}

}
