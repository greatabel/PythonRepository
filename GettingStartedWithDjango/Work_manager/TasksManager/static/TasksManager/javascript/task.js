function test(){
    alert('test');
}

$(function(){  
  
       $("#del1").bind('click',function(){  
           alert('test')
           $.ajax({  
                type:"GET",
                url:"http://127.0.0.1:8000/TasksManager/test/",  
                data:{name:'task1'},  
                dataType:"json",  
                success: function(data) {  
                    alert(data.msg)  
                }  
            });  
  
  
       })  
  
    })  