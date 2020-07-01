
public class PalindromeNumber {
	
	public boolean isPalindrome (int x) {
		String word = Integer.toString(x);
		
		char[] letters = new char[word.length()];
		
		for (int i=0; i < word.length(); i++) {
			letters[i] = word.charAt(i);
		}
		
		for (char ch : letters)
			System.out.println(ch);
		
		char[] reversed = new char[word.length()];
		
		for (int i=0; i < word.length(); i++)
			reversed[i] = letters[word.length()-i-1];
		
		for (char ch : reversed)
			System.out.println(ch);
		
		for (int i=0; i < word.length(); i++)
			if (letters[i] != reversed[i])
				return false;
		
		return true;
	}
	
	public boolean nonNegativePalindrome (int x) {
		
		int reversed = 0;
		int original = x;
		
		while (x != 0) {
			reversed = reversed * 10 + x % 10;
			x = x / 10;
			
			System.out.println("reversed: " + reversed + " x: " + x);
		}
		
		if (original == reversed)
			return true;
		else
			return false;
	}
	
	public boolean PalindromByIndexComparison (int x) {
		
		if (x < 0)
			return false;
		
		String integer = Integer.toString(x);
		int size = integer.length();
		
		for (int i=0, j=size-1; i <= j; i++, j--) {
			if (integer.charAt(i) != integer.charAt(j))
				return false;
		}
		
		return true;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		PalindromeNumber pn = new PalindromeNumber();
		
//		System.out.println(pn.nonNegativePalindrome(123));
//		System.out.println("==============");
//		System.out.println(pn.nonNegativePalindrome(121));
		
		System.out.println(pn.PalindromByIndexComparison(123));
		
	}

}
