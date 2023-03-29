package Push_Variante;

public class client {
    
    public static void main(String[] args) {
        station ws = new station();
        colorSignal signal = new colorSignal(ws);
        
        monitor m = new monitor(ws);
        ws.setHum(45.3f);
        ws.setTemp(22.5f);
        
        ws.setHum(80.0f);
        ws.setTemp(40.5f);
    }

}