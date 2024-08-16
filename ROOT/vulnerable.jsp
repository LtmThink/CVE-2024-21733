<%
        // 获取GET请求中的参数id
        String
        id = request.getParameter("id");
    
        // 打印出id的值
        if (id != null) {
        out.println("The ID is: " + id);
        } else {
        out.println("No ID parameter provided.");
        }
%>
