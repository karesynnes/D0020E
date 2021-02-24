using System.Collections;
using System.Collections.Generic;
using System.Net.Sockets;
using System.Net;
using System.Text;
using System;
using System.Threading;
using UnityEngine;

public class CommunicationScript : MonoBehaviour
{

    Dictionary<int,int[]> table = new Dictionary<int,int[]>();
    
    Thread widefindThread,fibaroThread;

    UdpClient fibaro, widefind;

    int fibaroPort = 42069;
    int widefindPort = 42070;

    Model model;


    // Start is called before the first frame update
    void Start()
    {
       
        init();

    }

    // Update is called once per frame
    void Update()
    {


    }

    void OnDestroy(){

        print("Killing recv thread");
        print("Killing sendThread");
        //widefindThread.Abort();
        fibaroThread.Abort();
    }

     private void init()
    {
        model = new Model();
       
        /*widefindThread = new Thread(new ThreadStart(ReceiveData));
        widefindThread.IsBackground = true;
        widefindThread.Start();*/
 

        fibaroThread = new Thread(new ThreadStart(fibaroComm));
        fibaroThread.IsBackground = true;
        fibaroThread.Start();
 
    }

    public Model getModel(){

        return this.model;
    }

    private void fibaroComm()
    {
        
        fibaro = new UdpClient(fibaroPort);
        fibaro.Connect("130.240.114.52",fibaroPort);

        string a = "fibaro;";

        int[] k = {299,271};
        int i = 0;
        
       
        IPEndPoint anyIP = new IPEndPoint(IPAddress.Any, 0);
        byte[] c;

        while(true){
             i = i%(k.Length);
            //print("Sending : " + a);
            a = "fibaro;" + k[i].ToString();
            i++;
           

            print("THIS IS a:" + a);

            c = Encoding.ASCII.GetBytes(a);
            Thread.Sleep(1000);
            print("SENDING : " + a);
            fibaro.Send(c, c.Length);



            byte[] data = fibaro.Receive(ref anyIP);
  
                
            string text = Encoding.UTF8.GetString(data);
            print("RECEIVING : " + text);
 
            model.updateTable(text);
                

        }


    }

    private void widefindComm(){

        widefind = new UdpClient(widefindPort);

        fibaro.Connect("130.240.114.52",widefindPort);

        string a = "widefind;2"; //2 är bara temporärt

        byte[] c = Encoding.ASCII.GetBytes(a);
        IPEndPoint anyIP = new IPEndPoint(IPAddress.Any, 0);

        while(true){

            Thread.Sleep(1000);

            widefind.Send(c, c.Length);

            byte[] data = widefind.Receive(ref anyIP);
  
                
            string text = Encoding.UTF8.GetString(data);

            model.updateTable(text);
            

        }


    }


}

