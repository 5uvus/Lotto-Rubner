package Factory;

public class HamburgPizzeria extends Pizzeria{

	@Override
	protected CreatePizza createPizza(String zuHolendePizza) {
		CreatePizza p = null;
		if (zuHolendePizza.equals("Calzone"))
			p = new HamburgCalzone();
		else if (zuHolendePizza.equals("Salami")) {
	    	p = new HamburgSalami();
	       
	    }
	    return p; 
	} 
}
