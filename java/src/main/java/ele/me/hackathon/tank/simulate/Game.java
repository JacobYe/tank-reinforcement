package ele.me.hackathon.tank.simulate;

import ele.me.hackathon.tank.GameEngine;
import org.apache.http.*;
import org.apache.http.impl.bootstrap.HttpServer;
import org.apache.http.impl.bootstrap.ServerBootstrap;
import org.apache.http.protocol.HttpContext;
import org.apache.http.protocol.HttpRequestHandler;
import org.apache.http.util.EntityUtils;

import java.io.IOException;
import java.net.URL;

/**
 * @author zhiming.rong
 */
public class Game {
    public static void main(String[] args) throws Exception{

//        URL mapUrl = Game.class.getResource("/map/firstweekmap.txt");
        URL mapUrl = Game.class.getResource("/map/secondweekmap.txt");
        System.out.println(mapUrl);
        String file = mapUrl.getFile();
        System.out.println(file);

        args = new String[]{
                file,
                "4",
                "1",
                "1",
                "3",
                "1",
                "1",
                "200",
                "2000",
                "localhost:9100",
                "localhost:9101"
        };

        GameEngine.main(args);
    }
}
