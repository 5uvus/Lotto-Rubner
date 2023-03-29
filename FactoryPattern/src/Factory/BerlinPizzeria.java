package Factory;

public class BerlinPizzeria extends Pizzeria {
	

	@Override
	protected CreatePizza createPizza(String zuHolendePizza) {
		CreatePizza p = null;
		if (zuHolendePizza.equals("Calzone"))
			p = new BerlinCalzone();
		else if (zuHolendePizza.equals("Salami")) {
	    	p = new BerlinSalami();
	       
	    }
	    return p; 
	} 
}
