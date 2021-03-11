using System.Collections;
using System.Collections.Generic;
using System;
using UnityEngine;

public class drawerScript : SensorScript
{
    private GameObject a;
    private int open;
    CommunicationScript script;
    private int yeboi;
    Vector3 startingPosition;
    Vector3 newPosition;
    //private Renderer cubeRenderer;

    public drawerScript()
    {
        this.open = 0;
        this.yeboi = 0;
        //this.cubeRenderer = null;
    }
    // Start is called before the first frame update
    void Start()
    {
        newPosition = new Vector3(transform.position.x, transform.position.y, transform.position.z + 5);
        startingPosition = transform.position;
        a = GameObject.Find("Main Camera");
        script = a.GetComponent<CommunicationScript>();

        //Create a new cube primitive to set the color on
        //this.cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
        //this.cube = transform.;

        //Get the Renderer component from the new cube
        //this.cubeRenderer = cube.GetComponent<Renderer>();

        //Call SetColor using the shader property name "_Color" and setting the color to red
        //cubeRenderer.material.SetColor("_Color", Color.green);
    }

    // Update is called once per frame
    void Update()
    {
        var cubeRenderer = this.GetComponent<Renderer>();
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
                transform.position = newPosition;
                //transform.SetPositionAndRotation(new Vector3(0, 0, yeboi), new Quaternion());

                //Get the Renderer component from the new cube


                //Call SetColor using the shader property name "_Color" and setting the color to red
                //cubeRenderer.material.SetColor("_Color", Color.green);

            }
            else
            {
                transform.position = startingPosition;
                //cubeRenderer.material.SetColor("_Color", Color.blue);
                //transform.eulerAngles = new Vector3(transform.eulerAngles.x, 180, transform.eulerAngles.z);
            }

        }
        catch (Exception e)
        {
            print(e);


        }
    }
}