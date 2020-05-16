package com.bober;

import com.bober.model.Species;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@WebServlet(
        name = "selectspeciesservlet",
        urlPatterns = "/SelectPet"
)

public class SelectSpeciesServlet extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

        String species = req.getParameter("Type");

        PetService petService = new PetService();
        Species l = Species.valueOf(species);

        List pets = petService.getAvailablePets(l);

        req.setAttribute("pets", pets);
        RequestDispatcher view = req.getRequestDispatcher("result.jsp");
        view.forward(req, resp);

    }
}
