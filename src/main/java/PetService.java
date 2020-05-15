package com.bober;

import com.bober.model.Species;

import java.util.ArrayList;
import java.util.List;


public class PetService {

    public List getAvailablePets(Species type){

        List pets = new ArrayList();

        if(type.equals(Species.CAT)){
            pets.add("Adrianna Vineyard");
            pets.add(("J. P. Chenet"));

        }else if(type.equals(Species.DOG)){
            pets.add("Glenfiddich");
            pets.add("Johnnie Walker");

        }else if(type.equals(Species.FISH)){
            pets.add("Corona");

        }else {
            pets.add("No Brand Available");
        }
        return pets;
    }
}
