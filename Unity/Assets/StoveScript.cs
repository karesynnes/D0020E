using System.Collections;
using System;
using System.Collections.Generic;
using UnityEngine;

public class StoveScript : SensorScript
{
    private int watt;
    GameObject a;
    CommunicationScript script;
    private Color red = new Color(1, 0, 0);
    private Color grey = new Color(1, 1, 1);
    GameObject one;
    GameObject two;
    GameObject three;
    GameObject four;
    public StoveScript()
    {

        this.watt = 0;



    }
    // Start is called before the first frame update
    void Start()
    {
        a = GameObject.Find("Main Camera");
        one = GameObject.Find("one");
        two = GameObject.Find("two");
        three = GameObject.Find("three");
        four = GameObject.Find("four");

        script = a.GetComponent<CommunicationScript>();
    }

    // Update is called once per frame
    void Update()
    {
     
        try
        {

            this.watt = script.getModel().getInfo(base.sensorID)[1];    
            


            if (this.watt > 10)
            {
                one.GetComponent<Renderer>().material.SetColor("_Color",red);
                two.GetComponent<Renderer>().material.SetColor("_Color", red);
                three.GetComponent<Renderer>().material.SetColor("_Color", red);
                four.GetComponent<Renderer>().material.SetColor("_Color", red);

            }
            else
            {
                one.GetComponent<Renderer>().material.SetColor("_Color", grey);
                two.GetComponent<Renderer>().material.SetColor("_Color", grey);
                three.GetComponent<Renderer>().material.SetColor("_Color", grey);
                four.GetComponent<Renderer>().material.SetColor("_Color", grey);
            }

        }
        catch (Exception e)
        {
             print(base.sensorID + " :" + e);


        }
    }
}
