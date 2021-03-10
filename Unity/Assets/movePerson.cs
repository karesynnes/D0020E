using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class movePerson : SensorScript
{
    Vector3 pos = new Vector3(0, 0, 0.05f);
    // Start is called before the first frame update

    GameObject a;
    CommunicationScript script;


    void Start()
    {

        a = GameObject.Find("Main Camera");

        script = a.GetComponent<CommunicationScript>();
        
    }

    // Update is called once per frame
    void Update()
    {
        int [] newPos = model.getInfo(base.sensorID);

        this.pos = new Vector3(newPos[0], newPos[1], newPos[2]);
        
        transform.eulerAngles = this.pos;


    }
}
