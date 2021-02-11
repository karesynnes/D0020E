using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DoorScript : SensorScript
{

    private int open;

    public DoorScript(int sensorID, Model model) : base(sensorID, model){
        
        this.open = 0;

    }


    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
        this.open = base.model.getInfo(base.sensorID)[0];


        if(this.open == 1){
             transform.eulerAngles = new Vector3(transform.eulerAngles.x, 90, transform.eulerAngles.z);
        }
        else{
             transform.eulerAngles = new Vector3(transform.eulerAngles.x, 180, transform.eulerAngles.z);
        }

       
        
    }
}