package ele.me.hackathon.tank.simulate;

import ele.me.hackathon.tank.GameEngine;

import java.net.URL;

/**
 * @author zhiming.rong
 */
public class Game2 {
    public static void main(String[] args) throws Exception{

//        URL mapUrl = Game.class.getResource("/map/firstweekmap.txt");
        URL mapUrl = Game2.class.getResource("/map/secondweekmap.txt");
        System.out.println(mapUrl);
        String file = mapUrl.getFile();
        System.out.println(file);

        args = new String[]{
                file,
                "4",
                "2",
                "4",
                "1",
                "1",
                "1",
                "100",
                "2000",
                "localhost:32770",
                "localhost:9101"
        };

        GameEngine.main(args);
    }
}
