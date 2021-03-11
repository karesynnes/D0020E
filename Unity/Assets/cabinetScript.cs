using System.Collections;
using System;
using System.Collections.Generic;
using UnityEngine;

public class cabinetScript : SensorScript
{
    int angle = 80;
    Transform left;
    Transform right;
    private int open;
    GameObject a;
    CommunicationScript script;


    public cabinetScript()
    {

        this.open = 0;



    }


    // Start is called before the first frame update
    void Start()
    {
        a = GameObject.Find("Main Camera");

        script = a.GetComponent<CommunicationScript>();
        left = transform.Find("left");
        right = transform.Find("right");
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

            //print(this.open);       


            if (this.open == 1)
            {
                left.eulerAngles = new Vector3(left.eulerAngles.x, left.eulerAngles.y, angle);
                right.eulerAngles = new Vector3(right.eulerAngles.x, right.eulerAngles.y, -angle);
            }
            else
            {
                left.eulerAngles = new Vector3(left.eulerAngles.x, left.eulerAngles.y, 0);
                right.eulerAngles = new Vector3(right.eulerAngles.x, right.eulerAngles.y, 0);
            }

        }
        catch (Exception e)
        {
            print(base.sensorID + " :" + e);


        }

    }
}