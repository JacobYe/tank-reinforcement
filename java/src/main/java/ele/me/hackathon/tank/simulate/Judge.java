package ele.me.hackathon.tank.simulate;

import ele.me.hackathon.tank.GameEngine;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.net.URL;
import java.util.Arrays;

/**
 * @author zhiming.rong
 */
public class Judge {
    Logger LOG_JUDGE = LoggerFactory.getLogger("JUDGE");
    Logger LOG_REPLAY = LoggerFactory.getLogger("REPLAY");

    String[] args;
    String PLAYER_A = "localhost:9100";
    String PLAYER_B = "localhost:9101";
    int TANK_NUM = 4;

    long[] totalA = new long[]{0,0,0,0};
    long[] totalB = new long[]{0,0,0,0};

//    int LOOP = 100000;
    int LOOP = 100;

    public Judge(){
//        URL mapUrl = Game.class.getResource("/map/firstweekmap.txt");
        URL mapUrl = Game.class.getResource("/map/samplemap.txt");
        LOG_JUDGE.debug(mapUrl.toString());
        String file = mapUrl.getFile();
        LOG_JUDGE.debug(file);

        args = new String[]{
                file,
                String.valueOf(TANK_NUM),
                "1",
                "1",
                "3",
                "1",
                "1",
                "100",
                "2000",
                PLAYER_A,
                PLAYER_B
        };
    }


    public void run(){
        GameEngine gameEngine = new GameEngine();
        gameEngine.init(args);

        for (int epoch = 0; epoch< LOOP; epoch++){
            LOG_REPLAY.info("*****[EpochStart {} ]*****", epoch);
            gameEngine.initEach();
            if(epoch % (LOOP/10) == 0){
                LOG_JUDGE.debug("{}", epoch);
            }
            GameEngine.JudgeResultCallBack callBack = gameEngine.new JudgeResultCallBack();
            gameEngine.setCallBack(callBack);
            gameEngine.start();
            long[] rstA = callBack.calc(PLAYER_A);
            long[] rstB = callBack.calc(PLAYER_B);

            LOG_JUDGE.debug("**[Round] " + epoch + "**");
            LOG_JUDGE.debug(Arrays.toString(rstA));
            LOG_JUDGE.debug(Arrays.toString(rstB));

            for(int i = 1; i<=3 ;i ++){
                totalA[i] = totalA[i] + rstA[i];
                totalB[i] = totalB[i] + rstB[i];
            }
            if(rstA[0] == rstB[0]){

            }else if(rstA[0] > rstB[0]){//A获胜
                totalA[0] = totalA[0] + 1;
            }else{
                totalB[0] = totalB[0] + 1;
            }
            LOG_REPLAY.info("*****[EpochEnd {} ]*****", epoch);
        }
    }

    public void score(){
        LOG_JUDGE.debug("**TOTAL**");
        LOG_JUDGE.debug(Arrays.toString(totalA));
        LOG_JUDGE.debug(Arrays.toString(totalB));
        LOG_JUDGE.info("{} VS {}.", PLAYER_A, PLAYER_B);
        LOG_JUDGE.info("[win]  {}", totalA[3] == totalB[3] ? "draw": (totalA[3] > totalB[3]? "PLAYER_1": "PLAYER_2"));
        LOG_JUDGE.info("[Loop] {}", LOOP);

        LOG_JUDGE.info("name\t\twin(%)\tsur(%)\tatk(%)\tflag");
        LOG_JUDGE.info("{}\t\t{}\t{}\t{}\t{}",
                "PY_1",
                String.format("%.2f", Double.valueOf(totalA[0])/LOOP),
                String.format("%.2f", Double.valueOf(totalA[1])/TANK_NUM/LOOP),
                String.format("%.2f", Double.valueOf(totalA[2])/TANK_NUM/LOOP),
                String.format("%.2f", Double.valueOf(totalA[3])/LOOP));
        LOG_JUDGE.info("{}\t\t{}\t{}\t{}\t{}",
                "PY_2",
                String.format("%.2f", Double.valueOf(totalB[0])/LOOP),
                String.format("%.2f", Double.valueOf(totalB[1])/TANK_NUM/LOOP),
                String.format("%.2f", Double.valueOf(totalB[2])/TANK_NUM/LOOP),
                String.format("%.2f", Double.valueOf(totalB[3])/LOOP));
    }

    public static void main(String[] args) {
        Judge judge = new Judge();
        judge.run();
        judge.score();
    }
}
