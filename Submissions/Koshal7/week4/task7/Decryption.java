import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Scanner;

public class Decryption {

	public static void main(String[] args)
		throws FileNotFoundException, IOException
	{
		Scanner sc = new Scanner(System.in);
		System.out.println(
			"Note : Encryption Key act as Password to Decrypt the same Image, otherwise it will corrupt the Image.");
		
		System.out.print("Enter a key for Decryption : ");
		int key = sc.nextInt();
		
		// Selecting a Image for Decryption.
		
		FileInputStream fis = new FileInputStream(
		"C:\\Users\\kapil\\Downloads\\batman.jpeg");
		
		// Converting image into byte array,it will
		// Create a array of same size as image.
		byte data[] = new byte[fis.available()];
		
		// Read the array
		
		fis.read(data);
		int i = 0;
		
		// Performing an XOR operation
		// on each value of
		// byte array to Decrypt it.
		for (byte b : data) {
			data[i] = (byte)(b ^ key);
			i++;
		}
		
		// Opening file for writing purpose
		FileOutputStream fos = new FileOutputStream(
			"C:\\Users\\kapil\\Downloads\\batman.jpeg");
		
		// Writing Decrypted data on Image
		fos.write(data);
		fos.close();
		fis.close();
		System.out.println("Decryption Done...");
	}
}
