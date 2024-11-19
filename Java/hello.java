import java.io.File;
public class hello {
    public static void main(String[] args) {
			File currentDir=new File(".");
			System.out.println(currentDir);
			 File[] directories = currentDir.listFiles(File::isDirectory);
			 if (directories != null) {
				for (File directory : directories) {
                System.out.println(directory.getName());
			 }}
      
            System.out.println("HOME environment variable is not set.");
        
    }
}