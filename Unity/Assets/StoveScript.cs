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
    private Color green = new Color(0, 1, 0);
    public StoveScript()
    {

        this.watt = 0;



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
        var rend = this.GetComponent<Renderer>();
        try
        {

            this.watt = script.getModel().getInfo(base.sensorID)[0];    


            if (this.watt > 0)
            {
                rend.material.SetColor("_Color",red);
            }
            else
            {
                rend.material.SetColor("_Color", green);
            }

        }
        catch (Exception e)
        {
            print(e);


        }
    }
}
