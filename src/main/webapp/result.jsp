<%@ page import ="java.util.*" %>
<!DOCTYPE html>
<html>
<body>
<center>
<h1>
    Available Pets
</h1>
<%
List result= (List) request.getAttribute("pets");
Iterator it = result.iterator();
out.println("<br>We have<br><br>");
while(it.hasNext()){
out.println(it.next()+"<br>");
}
%>
</body>
</html>