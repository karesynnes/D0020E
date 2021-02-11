using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DoorScript : SensorScript
{

    private bool open;

    public DoorScript(int sensorID, Model model) : base(sensorID, model){
        
        this.open = false;

    }


    public void toggleOpen(){

        if(this.open = false){
            this.open = true;
        } 
        else{
            this.open = false;
        }

    }

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {

        
        
    }
}
