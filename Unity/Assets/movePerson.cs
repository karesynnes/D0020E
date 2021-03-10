using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class movePerson : SensorScript
{
    Vector3 pos = new Vector3(0, 0, 0.05f);
    // Start is called before the first frame update

    GameObject a;
    CommunicationScript script;
    int[] newPos;

    void Start()
    {
        newPos = new int[] {0,0,0};
        a = GameObject.Find("Main Camera");

        script = a.GetComponent<CommunicationScript>();
        
    }

    // Update is called once per frame
    void Update()
    {
        //newPos = model.getInfo(base.sensorID);
        newPos[0] = (-1) * script.getModel().getInfo(-1)[1]/100 - 35;
        newPos[1] = script.getModel().getInfo(-1)[2]/200;
        newPos[2] = script.getModel().getInfo(-1)[0]/120 - 26;
        //this.pos = new Vector3(newPos[0], 6, newPos[2]);
        
        this.transform.position = new Vector3(newPos[0], 6, newPos[2]);


    }
}
