using System.Collections;
using System;
using System.Collections.Generic;
using UnityEngine;

public class FridgeScript : SensorScript
{
    int angle = 90;
    private int open;
    GameObject a;
    CommunicationScript script;


    public FridgeScript()
    {

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
        try
        {
            //print(script.getModel().getInfo(base.sensorID));
            //print(base.sensorID);

            this.open = script.getModel().getInfo(base.sensorID)[0];

            //print(base.sensorID + " open " + this.open);       


            if (this.open == 1)
            {
                var angles = gameObject.transform.eulerAngles;
                angles.Set(-90, 90, 90);
                gameObject.transform.eulerAngles = angles;
            }
            else
            {
                var angles = gameObject.transform.eulerAngles;
                angles.Set(-90, 90, 0);
                gameObject.transform.eulerAngles = angles;
            }

        }
        catch (Exception e)
        {
            print(base.sensorID + " :" + e);


        }

    }
}