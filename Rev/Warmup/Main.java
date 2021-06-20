import java.util.*;
import java.lang.*;

public class Main {
  
	public static String cold(String t) {
		return t.substring(17) + t.substring(0, 17);
	}
	
	public static ArrayList<String> coldrev(ArrayList<String> arr) {
	    ArrayList<String> revd = new ArrayList<String>();
	    
	    for(String t : arr){
		    revd.add(t.substring(16) + t.substring(0, 16));
	    }
	    return revd;
	}
	
	public static String cool(String t) {
		String s = "";
		for (int i = 0; i < t.length(); i++)
			if (i % 2 == 0)
				s += (char) (t.charAt(i) + 3 * (i / 2));
			else
				s += t.charAt(i);
		return s;
	}
	
	public static ArrayList<String> coolrev(ArrayList<String> arr) {
		ArrayList<String> revd = new ArrayList<String>();
		
		for(String t :arr){
    		String s = "";
    		for (int i = 0; i < t.length(); i++)
    			if (i % 2 == 0)
    				s += (char) (t.charAt(i) - 3 * (i / 2));
    			else
    				s += t.charAt(i);
    		revd.add(s);
		}
		return revd;
	}
		
	public static String warm(String t) {
		String a = t.substring(0, t.indexOf("l") + 1);
		String t1 = t.substring(t.indexOf("l") + 1);
		String b = t1.substring(0, t1.indexOf("l") + 1);
		String c = t1.substring(t1.indexOf("l") + 1);
		return c + b + a;
	}
	
	public static ArrayList<String> warmrev(String orig) {
		//String orig = "|g1c3[s]_^nyyk0u_GyJ}~l3nwh:l";
		
		ArrayList<String> revd = new ArrayList<String>();
		String bpc = orig.substring(0, orig.indexOf("l") + 1);
		String a = orig.substring(orig.indexOf("l") + 1);
		String c , b ;
		
		for(int i = 0; i<bpc.length(); i++){
		    c = bpc.substring(0, i);
		    b = bpc.substring(i);
		    
		    revd.add(a+b+c);
		}
		
		//System.out.println(revd);
		return revd;
	}
	
	public static String hot(String t) {
		int[] adj = {-72, 7, -58, 2, -33, 1, -102, 65, 13, -64, 
				21, 14, -45, -11, -48, -7, -1, 3, 47, -65, 3, -18, 
				-73, 40, -27, -73, -13, 0, 0, -68, 10, 45, 13};
		String s = "";
		for (int i = 0; i < t.length(); i++)
			s += (char) (t.charAt(i) + adj[i]);
		return s;
	}
	
	public static String hotrev(String t) {
		int[] adj = {-72, 7, -58, 2, -33, 1, -102, 65, 13, -64, 
				21, 14, -45, -11, -48, -7, -1, 3, 47, -65, 3, -18, 
				-73, 40, -27, -73, -13, 0, 0, -68, 10, 45, 13};
		String s = "";
		for (int i = 0; i < t.length(); i++)
			s += (char) (t.charAt(i) - adj[i]);
		return s;
	}

	public static void main(String[] args) {
		//Scanner in = new Scanner(System.in);
		//System.out.print("Let's get warmed up! Please enter the flag: ");
		//String flag = in.nextLine();
		String match = "4n_3nd0th3rm1c_rxn_4b50rb5_3n3rgy";
		
		// hot(warm(cool(cold(flag)))) = (match)
		// warm(cool(cold(flag))) = hotrev(match)
		// (cool(cold(flag))) = warmrev(hotrev(match)))
		// (cold(flag))) = coolrev(warmrev(hotrev(match))))
		// (flag) = coldrev(coolrev(warmrev(hotrev(match)))))
		
		ArrayList<String> reversed = coldrev(coolrev(warmrev(hotrev(match)))) ;
		
		for(String flag: reversed){
		    String temp = hot(warm(cool(cold(flag))));
		    //System.out.println(temp);
    		if (flag.length() == 33 && temp.equals(match))
    			System.out.println("this : "+flag);
		}
	}
  
}
