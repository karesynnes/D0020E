using System.Collections;
using System.Collections.Generic;
using System;
using UnityEngine;

public class Model
{



    //Modell för information. Relevant information sparas baserat på nyckeln, ID. 
    //Objekt som ärft klassen SensorObject kommer hämta information från denna modell varje(?) frame
    private Dictionary<int, int[]> table;

    public Model(){

        table = new Dictionary<int, int[]>();

    }

    public int getTest(){
        return 2;
    }

    public void addItem(int ID, string type){

        switch (type)
            {
                case "switch_sensor":
                    table[ID] = new int[2];

                    break;

                case "state_sensor":
                    Debug.Log("added id:" + ID);
                    table[ID] = new int[2];

                    break;
                    
                case "power_sensor":
                    table[ID] = new int[2];

                    break;
                
                case "other_sensor":
                    table[ID] = new int[1];

                    break;

                case "dual_sensor":
                    table[ID] = new int[4];

                    break;

            

                default:

                    //print("Some faulty type has entered the model!");
                    break;


            }

        //switch case baserat på ID


        //skapa en ny entry i table med key = ID och value = en array med storlek baserat på Type

    }

    public int[] getInfo(int sensorID){


        if(table.ContainsKey(sensorID)){
             return this.table[sensorID];
        }
        //hämta info från modellen baserat på nyckeln = ID
       else{
           throw new Exception("No such key");
       }

    }


    public void updateTable(string info){

        string[] values = info.Split(';');

        int sensorID = Int32.Parse(values[0]);
        

        if(table.ContainsKey(sensorID)){

            switch (values[1])
            {
                case "switch_sensor":
                    table[sensorID] = new int[] {Int32.Parse(values[2]),Int32.Parse(values[3])};

                    break;

                case "state_sensor":
                    
                    if(bool.Parse(values[2])){
                         table[sensorID] = new int[] {1,Int32.Parse(values[3])};
                         
                    }
                    else{
                        table[sensorID] = new int[] {0,Int32.Parse(values[3])};
                       
                    }
                   

                    break;
                    
                case "power_sensor":
                    table[sensorID] = new int[] {Int32.Parse(values[2]),Int32.Parse(values[3])};

                    break;
                
                case "other_sensor":
                    table[sensorID] = new int[] {Int32.Parse(values[2])};

                    break;

                case "dual_sensor":
                    table[sensorID] = new int[] {Int32.Parse(values[2]),Int32.Parse(values[3]),Int32.Parse(values[4]),Int32.Parse(values[5])};

                    break;

            

                default:

                    //print("Some faulty type has entered the model!");
                    break;


            }


        }
        else{

            addItem(sensorID,values[1]);
        }


        //ta in informationen om sensorn

        //updatera fälten hos arrayen med nyckeln = ID

        //om ID inte finns i table så kalla på addItem()


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