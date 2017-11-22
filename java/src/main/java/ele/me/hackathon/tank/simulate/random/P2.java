package ele.me.hackathon.tank.simulate.random;

import ele.me.hackathon.tank.player.PlayerServer;
import org.apache.thrift.server.TServer;
import org.apache.thrift.server.TSimpleServer;
import org.apache.thrift.transport.TServerSocket;
import org.apache.thrift.transport.TServerTransport;

/**
 * @author zhiming.rong
 */
public class P2 {
    public static void main(String[] args) {
        TankRandomHandler handler = new TankRandomHandler();
        PlayerServer.Processor processor = new PlayerServer.Processor<>(handler);
        Runnable simple = new Runnable() {
            public void run() {
                simple(processor);
            }
        };
        new Thread(simple).start();
    }

    public static void simple(PlayerServer.Processor processor) {
        try {
            TServerTransport serverTransport = new TServerSocket(9101);
            TServer server = new TSimpleServer(new TServer.Args(serverTransport).processor(processor));

            // Use this for a multithreaded server
            // TServer server = new TThreadPoolServer(new TThreadPoolServer.Args(serverTransport).processor(processor));

            System.out.println("Starting the simple server...");
            server.serve();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
