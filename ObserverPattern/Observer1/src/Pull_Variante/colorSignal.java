package Pull_Variante;

public class colorSignal implements Observer {
    private station ws;

    public colorSignal(station ws){
        this.ws = ws;
        this.ws.addClient(this);
    }

    @Override
    public void update() {
        double newTemp = ws.getTemp();
        double newHumidity = ws.getHum();
        
        
        if (newTemp <= 35.0f){
            System.out.println("GRÜN");
        }else{
            System.out.println("ROT");
        }
        if (newHumidity <= 60.0f){
            System.out.println("GRÜN");
        }else{
            System.out.println("ROT");
        }
    }
}