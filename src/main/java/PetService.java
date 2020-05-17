package com.bober;

import com.bober.model.Species;

import java.util.ArrayList;
import java.util.List;


public class PetService {

    public List getAvailablePets(Species type){

        List pets = new ArrayList();

        if(type.equals(Species.CAT)){
            pets.add("Name: Tom | Age: 5 | Sex: M ");
            pets.add("Name: Lucy| Age: 2 | Sex: F ");

        }else if(type.equals(Species.DOG)){
            pets.add("Name: Barkley | Age: 4 | Sex: M ");
            pets.add("Name: Zoey    | Age: 8 | Sex: F ");

        }else if(type.equals(Species.FISH)){
            pets.add("Name: Alex | Age: 3m | Sex: ~ ");

        }else {
            pets.add("No Pets Available");
        }
        return pets;
    }
}
