package iperfer;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.ConnectException;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.nio.ByteBuffer;

public class Iperfer {

    int d = 0;

    public  void send(String h, int p, int t) throws IOException, InterruptedException {

        Socket socket = new Socket();
        long record_of_bytes_sent = 0;

        try {
            socket.connect(new InetSocketAddress(h, p
         ));
        } catch (ConnectException ex) {
            System.out.println("The program cannot conect to the server.");
            System.exit(-3);
        }
        OutputStream os = socket.getOutputStream();
        DataOutputStream dataoutputstream = new DataOutputStream(os);

        long maxTime = (long) t;
//        calculating time in mili seconds , 
//         starting time
        long st = System.currentTimeMillis();
//        Current time
        long ct = System.currentTimeMillis();
//        total Time taken
        long tt = 1;

        byte[] stream_data;
        stream_data = ByteBuffer.allocate(1024).putInt(d).array();
        maxTime = maxTime * 1000;

        while (maxTime >= (tt = st - ct)) {

            dataoutputstream.write(stream_data);
//            flusing data
            dataoutputstream.flush();
//          current time
            ct = System.currentTimeMillis();

            record_of_bytes_sent = record_of_bytes_sent + stream_data.length;

        }

        dataoutputstream.close();

        socket.close();

        tostring(record_of_bytes_sent, (float) (record_of_bytes_sent / tt));

    }

    public  void tostring(long sent, float rate) {
        System.out.println("sent=" + sent / 1000.0 + " KB rate=" + 8 * rate / 1000.0 + " Mbps");
    }

    private static boolean checkportrange(int p) {
        return p >= 1024 && p < 65536;
    }

    private static boolean checktime(int t) {
        return t >= 0;
    }

    public static void main(String[] args) throws IOException, InterruptedException {
        
        
        Iperfer iperf = new Iperfer();
        
        int totalArguments = args.length;

        if (totalArguments != 0) {
        } else {
            System.out.println("Error: missing or additional arguments");
            System.exit(-2);
        }

        String hostname = args[0];
        int port = Integer.parseInt(args[1]);

        if (!checkportrange(port)) {
            System.out.println("Error: port number must be in the range 1024 to 65535");
            System.exit(-1);

        }
        int time = Integer.parseInt(args[2]);

        if (!checktime(time)) {
            System.out.println("Invalid time");
            System.exit(-1);
        }
        
        iperf.send(hostname,port,time);
        

    }
}
