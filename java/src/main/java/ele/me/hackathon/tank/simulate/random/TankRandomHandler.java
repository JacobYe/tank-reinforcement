package ele.me.hackathon.tank.simulate.random;

import ele.me.hackathon.tank.player.Direction;
import ele.me.hackathon.tank.player.Args;
import ele.me.hackathon.tank.player.GameState;
import ele.me.hackathon.tank.player.Order;
import ele.me.hackathon.tank.player.PlayerServer;
import org.apache.thrift.TException;
import org.apache.thrift.server.TServer;
import org.apache.thrift.server.TSimpleServer;
import org.apache.thrift.transport.TServerSocket;
import org.apache.thrift.transport.TServerTransport;

import java.util.*;
import java.util.stream.Collectors;

/**
 * @author zhiming.rong
 */
public class TankRandomHandler implements PlayerServer.Iface{

    List<Integer> tanks;

    List<String> orders = new ArrayList<>(3);

    Random rand = new Random();


    public TankRandomHandler(){
//        orders.add("fire");
        orders.add("turnTo");
        orders.add("move");
    }

    @Override
    public void uploadMap(List<List<Integer>> gamemap) throws TException {

    }

    @Override
    public void uploadParamters(Args arguments) throws TException {

    }

    @Override
    public void assignTanks(List<Integer> tanks) throws TException {
        System.out.println(tanks);
        this.tanks = tanks;
    }

    @Override
    public void latestState(GameState state) throws TException {

    }

    @Override
    public List<Order> getNewOrders() throws TException {
        return tanks.stream().map(id -> randomMove(id)).collect(Collectors.toList());
    }


    private Order randomMove(int id){
        String order = orders.get(rand.nextInt(orders.size()));//TODO size to private param
        Direction direction = Direction.values()[rand.nextInt(Direction.values().length)];
        return new Order(id, order, direction);
    }

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
