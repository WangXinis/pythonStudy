public class HomeDirectoryExample {
    public static void main(String[] args) {
        // 获取HOME环境变量的值
        String homeDirectory = System.getenv("HOME");
 
        // 如果HOME环境变量存在，则打印其值
        if (homeDirectory != null) {
            System.out.println("Home directory is: " + homeDirectory);
        } else {
            System.out.println("HOME environment variable is not set.");
        }
    }
}