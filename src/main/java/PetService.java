package com.bober;

import com.bober.model.Species;

import java.util.ArrayList;
import java.util.List;


public class PetService {

    public List getAvailablePets(Species type){

        List pets = new ArrayList();

        if(type.equals(Species.CAT)){
            pets.add("Name: Tom     | Age: 5y | Sex: M ");
            pets.add("Name: Lucy    | Age: 2y | Sex: F ");

        }else if(type.equals(Species.DOG)){
            pets.add("Name: Barkley | Age: 4y | Sex: M ");
            pets.add("Name: Zoey    | Age: 8y | Sex: F ");

        }else if(type.equals(Species.FISH)){
            pets.add("Name: Alex    | Age: 3m | Sex: ~ ");

        }else {
            pets.add("No Pets Available");
        }
        return pets;
    }
}
