using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class movePerson : MonoBehaviour
{
    Vector3 pos = new Vector3(0, 0, 0.05f);
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        //ta in widefind här och uppdatera positionen med dem.
        transform.position += pos;
    }
}
