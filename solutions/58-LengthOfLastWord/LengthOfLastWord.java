
public class LengthOfLastWord {
	
	public int lengthOfLastWord (String s) {
		
		if (s.length() == 0 || s.isBlank())
			return 0;
		else if (s.indexOf(" ") == -1) { // No space == one word
			return s.length();
		} else {
			String[] words = s.split(" ");
			return words[words.length-1].length();
			
		}
		
    } 

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		LengthOfLastWord lolw = new LengthOfLastWord();
		System.out.println(lolw.lengthOfLastWord("Hello World"));

	}

}
