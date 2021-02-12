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
    
    Thread recvThread,sendThread;

    UdpClient client, send;

    int port = 42069;

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
        recvThread.Abort();
        sendThread.Abort();
    }

     private void init()
    {
        model = new Model();
       
        recvThread = new Thread(new ThreadStart(ReceiveData));
        recvThread.IsBackground = true;
        recvThread.Start();
 

        sendThread = new Thread(new ThreadStart(SendData));
        sendThread.IsBackground = true;
        sendThread.Start();
 
    }

    public Model getModel(){

        return this.model;
    }

    private void SendData()
    {
        send = new UdpClient("130.240.114.52",port);

        string a = "fibaro;299";
        
        byte[] c = Encoding.ASCII.GetBytes(a);


        while(true){

            print("Sending : " + a);

            send.Send(c, c.Length);

        }


    }

    private void ReceiveData()
    {
       
        client = new UdpClient(port);
        while (true)
        {
 
            try
            {

                
                IPEndPoint anyIP = new IPEndPoint(IPAddress.Any, 0);
                byte[] data = client.Receive(ref anyIP);
 

 
                
                string text = Encoding.UTF8.GetString(data);
                print("Receiving : " + text);
 
                model.updateTable(text);




                print(">> " + text);

                if(text.Equals("stop")){
                    break;
                }
               
               
               
            }
            catch (Exception err)
            {
                print(err.ToString());
            }
        }
    }



}

