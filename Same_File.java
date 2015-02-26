import java.io.*;
import java.util.*;

public class Same_File {
	public ArrayList<Integer> isEqual(String path1, String path2) {
		ArrayList al=new ArrayList<Integer>();
		try {	
			Scanner sc=new Scanner(new File(path1));
			Scanner sc2=new Scanner(new File(path2));
			int i=0;
			while(sc.hasNext() && sc2.hasNext()) {
				String s=sc.next();
				String s2=sc2.next();
				if(!s.equals(s2)) al.add(i);
				i++;
			}
			sc.close();
			sc2.close();
		}catch(Exception e) {}
		return al;
	}
	public static void main(String args[]) {
		Same_File sf=new Same_File();
		System.out.println(sf.isEqual("BD/Equipements.json","BD/Activites.json"));
	}
}