import java.io.IOException;  
    import java.io.PrintWriter;  
    import javax.servlet.ServletException;  
    import javax.servlet.http.Cookie;  
    import javax.servlet.http.HttpServlet;  
    import javax.servlet.http.HttpServletRequest;  
    import javax.servlet.http.HttpServletResponse;  
    public class login extends HttpServlet {  
        protected void doPost(HttpServletRequest request, HttpServletResponse response)  
                               throws ServletException, IOException {  
            response.setContentType("text/html");  
            PrintWriter out=response.getWriter();  
              
            //request.getRequestDispatcher("index.html").include(request, response);  
              int k=0;
            String name=request.getParameter("username");  
            String password=request.getParameter("password");  
            if(name.equals("admin"))
            {
            if(password.equals("admin123")){  
                request.getRequestDispatcher("common.html").include(request, response);
//                out.print("<br>You are successfully logged in!");  
//                out.print("<br>Welcome, "+name);  
                
//                Cookie ck=new Cookie("name",name);  
//                response.addCookie(ck);  
            }else{
                if(password.isEmpty())
                {
                    
                k=1;
                }
                if(password.equals("$#ewqr#$")){
                
                //request.getRequestDispatcher("data1.html").include(request, response);
                }
                else
                {
                   k=1;
                }
                    
            }
            }
            else
            {
                k=1;
            }
        
            if(name.isEmpty())
            {
                k=1;
            }
         
           if(k==1)
           {
               request.getRequestDispatcher("login.html").include(request, response);  
                out.print("enter password or user name");  
           }
           else
           {
               
           }
              
            out.close();  
        }  
      
    }  
