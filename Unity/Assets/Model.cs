using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Model : MonoBehaviour
{



    //Modell för information. Relevant information sparas baserat på nyckeln, ID. 
    //Objekt som ärft klassen SensorObject kommer hämta information från denna modell varje(?) frame
    private Dictionary<int, int[]> table;

    public Model(){
        table = new Dictionary<int, int[]>();

    }

    public void addItem(int ID){

        //switch case baserat på ID


        //skapa en ny entry i table med key = ID och value = en array med storlek baserat på Type

    }

    public int[] getInfo(int sensorID){

        //hämta info från modellen baserat på nyckeln = ID


    }


    public void updateTable(string info){

        string[] values = info.Split(";");

        switch (values[1])
        {
            case "switch_sensor":

                break;

            case "state_sensor":

                break;
                
            case "power_sensor":

                break;
            
            case "other_sensor":

                break;

            case "dual_sensor":

                break;

        

            default:

                print("Some faulty type has entered the model!");
                break;


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
