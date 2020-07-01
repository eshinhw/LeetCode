
public class ValidPerfectSquare {
	
	public boolean isPerfectSquareV1 (int num) {
        
		int sum = 1;
		int addition = 3;
		
		if (num < 1 || num > Integer.MAX_VALUE)
			return false;
		
		while (sum <= num) {
			
			if (sum == num)
				return true;
			sum = sum + addition;
			addition = addition + 2;
		}
		
		return false;
		
		
    }
	
	public boolean isPerfectSquareV2 (int num) {
        
		
		
		if (num < 1 || num > Integer.MAX_VALUE)
			return false;
		
		int sum = 1;
		
		while ((sum*sum) <= num) {
			
			if ((sum*sum) == num)
				return true;
			
			sum++;
			
		}
		
		return false;
		
		
    }
	
	
	public static void main (String[] args) {
		// TODO Auto-generated method stub
		
		ValidPerfectSquare vps = new ValidPerfectSquare();
		
		System.out.println(vps.isPerfectSquareV2(16));
		System.out.println(vps.isPerfectSquareV2(14));
		

	}

}
