package Proxy;

public class Main {
	
	
 public static void main(String[] args) {
	 
	 Printer printer = new PrinterProxy();
	 printer.print("Page printed!"); // druckt in SW
	 ((PrinterProxy) printer).switchToColor();
	 printer.print("Page printed!"); // druckt in Farbe
}
}
