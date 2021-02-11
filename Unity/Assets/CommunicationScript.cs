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
    
    Thread recvThread;

    UdpClient client;

    int port = 42069;

    Model model = new Model();


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
        recvThread.Abort();
    }

     private void init()
    {
    
       
        recvThread = new Thread(new ThreadStart(ReceiveData));
        recvThread.IsBackground = true;
        recvThread.Start();
 
    }


    private  void ReceiveData()
    {
 
        client = new UdpClient(port);
        while (true)
        {
 
            try
            {
                
                IPEndPoint anyIP = new IPEndPoint(IPAddress.Any, 0);
                byte[] data = client.Receive(ref anyIP);
 
                
                string text = Encoding.UTF8.GetString(data);
 
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


