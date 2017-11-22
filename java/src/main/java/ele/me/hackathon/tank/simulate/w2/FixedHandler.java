package ele.me.hackathon.tank.simulate.w2;

import ele.me.hackathon.tank.player.*;
import ele.me.hackathon.tank.player.PlayerServer.Iface;
import org.apache.thrift.TException;
import org.apache.thrift.server.TServer;
import org.apache.thrift.server.TSimpleServer;
import org.apache.thrift.transport.TServerSocket;
import org.apache.thrift.transport.TServerTransport;

import java.util.*;

/**
 * @author zhiming.rong
 */
public class FixedHandler implements Iface {

    Map<Integer,List<Integer>> map = new HashMap<>();
    Map<Integer,Integer> map_default = new HashMap<>();
    List<Integer> tanks;

    public FixedHandler(){
        Integer[] a1 = new Integer[]{0,0,0,0,0,0,0,4,0,0,0,2,0,0,0,0,0};
        Integer[] a2 = new Integer[]{0,0,0};
        Integer[] a3 = new Integer[]{0,0,0,0,0,0,0,4,0,0,2,0,0,0,0,0};
        Integer[] a4 = new Integer[]{0,0,0,4,0,0,0,0,2,0,0,0,0};
        Integer[] a5 = new Integer[]{0,0,0,0,0,0,0,3,0,0,0,1,0,0,0,0,0};
        Integer[] a6 = new Integer[]{0,0,0};
        Integer[] a7 = new Integer[]{0,0,0,0,0,0,0,3,0,0,1,0,0,0,0,0};
        Integer[] a8 = new Integer[]{0,0,0,3,0,0,0,0,1,0,0,0,0};
        map.put(1, new LinkedList<>(Arrays.asList(a1)));
        map.put(2, new LinkedList<>(Arrays.asList(a2)));
        map.put(3, new LinkedList<>(Arrays.asList(a3)));
        map.put(4, new LinkedList<>(Arrays.asList(a4)));
        map.put(5, new LinkedList<>(Arrays.asList(a5)));
        map.put(6, new LinkedList<>(Arrays.asList(a6)));
        map.put(7, new LinkedList<>(Arrays.asList(a7)));
        map.put(8, new LinkedList<>(Arrays.asList(a8)));

        map_default.put(1,8);
        map_default.put(2,8);
        map_default.put(3,8);
        map_default.put(4,8);
        map_default.put(5,7);
        map_default.put(6,7);
        map_default.put(7,7);
        map_default.put(8,7);
    }

    @Override
    public void uploadMap(List<List<Integer>> gamemap) throws TException {

    }

    @Override
    public void uploadParamters(Args arguments) throws TException {

    }

    @Override
    public void assignTanks(List<Integer> tanks) throws TException {
        this.tanks = tanks;

    }

    @Override
    public void latestState(GameState state) throws TException {
        System.out.println(state);
    }

    @Override
    public List<Order> getNewOrders() throws TException {
        List<Order> rst = new ArrayList<>();
        for(Integer tank: tanks){
            Integer action;
            List<Integer> actions = map.get(tank);
            if(actions.isEmpty()){
                action = map_default.get(tank);
            }else{
                action = actions.remove(0);
            }
            rst.add(action2order(tank, action));
        }

        return rst;
    }

    public static Order action2order(int tankId, int i){
        switch (i){
            case 0:
                return new Order(tankId, "move", Direction.UP);
            case 1:
                return new Order(tankId, "turnTo", Direction.UP);
            case 2:
                return new Order(tankId, "turnTo", Direction.DOWN);
            case 3:
                return new Order(tankId, "turnTo", Direction.LEFT);
            case 4:
                return new Order(tankId, "turnTo", Direction.RIGHT);
            case 5:
                return new Order(tankId, "fire", Direction.UP);
            case 6:
                return new Order(tankId, "fire", Direction.DOWN);
            case 7:
                return new Order(tankId, "fire", Direction.LEFT);
            case 8:
                return new Order(tankId, "fire", Direction.RIGHT);
        }
        return new Order(tankId, "", Direction.UP);
    }

    public static void main(String[] args) {
        int port = 80;
        if(args.length > 0){
            try{
                port = Integer.valueOf(args[0]);
            }catch (Exception e){

            }
        }

        final int port_ = port;

        FixedHandler handler = new FixedHandler();
        PlayerServer.Processor processor = new PlayerServer.Processor<>(handler);
        Runnable simple = new Runnable() {
            public void run() {
                simple(processor, port_);
            }
        };
        new Thread(simple).start();
    }

    public static void simple(PlayerServer.Processor processor, int port) {
        try {
            TServerTransport serverTransport = new TServerSocket(port);
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
