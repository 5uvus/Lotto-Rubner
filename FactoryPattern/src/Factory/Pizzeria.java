package Factory;

public abstract class Pizzeria {
	 public CreatePizza holePizza(String zuHolendePizza) { 
	        //Delegation der Objekterstellung an Subklasse 
	        CreatePizza p = createPizza(zuHolendePizza); 

	        //weitere verarbeitung 
	        p.backen(); 
	        p.schneiden(); 
	        p.einpacken(); 
	       
	        return p; 
	    } 

	    //Definition der Factory Method 
	    protected abstract CreatePizza createPizza(String zuHolendePizza); 

}
