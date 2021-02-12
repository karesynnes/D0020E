using System.Collections;
using System;
using System.Collections.Generic;
using UnityEngine;

public class DoorScript : SensorScript
{

    private int open;
     GameObject a;
    CommunicationScript script;

   
    public DoorScript(int sensorID) : base(299){
        
        this.open = 0;
        

    }


    // Start is called before the first frame update
    void Start()
    {
        a = GameObject.Find("Main Camera");

        script = a.GetComponent<CommunicationScript>();
        
    }

    // Update is called once per frame
    void Update()
    {
       
        //this.open = base.model.getInfo(base.sensorID)[0];
       // print(base.model.getTest());
       try{
       print(script.getModel().getInfo(base.sensorID));
        

        if(this.open == 1){
             transform.eulerAngles = new Vector3(transform.eulerAngles.x, 90, transform.eulerAngles.z);
        }
        else{
             transform.eulerAngles = new Vector3(transform.eulerAngles.x, 180, transform.eulerAngles.z);
        }

       }
       catch(Exception e){
          // print(e);


       }
        
    }
}