import java.io.*;

public class strings {
	
	public static void main (String[] args) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		String nombre;
		int i;
		int j;
		System.out.print("Introduce una palabra: ");
		nombre = reader.readLine();
		
		for (i=0;i<nombre.length();i++) {
			for (j=nombre.length()-1;j>i;j--){
				System.out.print("··");
			}
			for (j=0;j<=i;j++){
				if (j==i){
					System.out.print(nombre.charAt(j)+"="+nombre.charAt(j));
				} else {
				System.out.print(nombre.charAt(j)+",");
				}
			}
			for (j=i-1;j>=0;j--){
				System.out.print(","+nombre.charAt(j));
			}
			for (j=nombre.length()-1;j>i;j--){
				System.out.print("··");
			}
			System.out.println();								
		}
	}
}

