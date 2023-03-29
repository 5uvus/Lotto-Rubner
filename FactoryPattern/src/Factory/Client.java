package Factory;

public class Client {
	public static void main(String[] args) { 
        Pizzeria hamburg = new HamburgPizzeria(); 
        CreatePizza hSalami = hamburg.createPizza("Salami"); 
        hSalami.backen();//"Pages startet" 
        hSalami.schneiden();
        hSalami.einpacken();
        
        Pizzeria berlin = new BerlinPizzeria(); 
        CreatePizza bCalzone = berlin.createPizza("Calzone"); 
        bCalzone.backen();//"Powerpoint startet" 
        bCalzone.schneiden();
        bCalzone.einpacken();
    } 
}
