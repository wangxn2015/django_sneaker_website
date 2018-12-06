$(document).ready(function(){

    var current_url, dest_url;
    current_url = window.location.pathname;


    $("#profile_button").click(function () {
        // $("#data_div").get(dest_url, function(data){
        //     $(this).(data)
        dest_url = current_url+'profile/';
         $.ajax({
             type: "GET",
             url: dest_url,
             // data: {username:$("#username").val(), content:$("#content").val()},
             dataType: "json",
             success: function(data){
                 $('#data_div').empty();   //清空resText里面的所有内容
                 // $('#data_div').html(data.user_id);
                 // $('#data_div').html(data.user_name);
                 // $('#data_div').html(data.user_birth);
                 // $('#data_div').html(data.user_des);
                 var len = data.len
                 var tableStr = "<table class='tab-list' width='99%'>";

                 tableStr = tableStr
                   + "<tr class='list-header'>"
                   +"<td width='5%'><b>UserID</b></td>"
                   +"<td width='10%'><b>UserName</b></td>"
                   +"<td width='10%'><b>Birthday</b></td>"
                   +"<td width='10%'><b>Description</b></td>"
                   +"</tr>";

                 // for ( var i = 0; i < len; i++) {
                  tableStr = tableStr + "<tr>"
                    // +"<td>"+ (i+1) + "</td>"
                    +"<td>"+ data.user_id + "</td>"
                    + "<td>"+ data.user_name + "</td>"
                    + "<td>"+ data.user_birth + "</td>"
                    +"<td>"+data.user_des+"</td>"
                    +"</tr>";
                 // }
                 if(len==0){
                  tableStr = tableStr + "<tr style='text-align: center'>"
                  +"<td colspan='6'><font color='#cd0a0a'>"+ 暂无记录 + "</font></td>"
                  +"</tr>";
                 }
                 tableStr = tableStr + "</table>";
                 //添加到div中
                 $("#data_div").html(tableStr);
                 },
         });

    });
////////////////////////
    //
    $("#manage_button").click(function () {
        dest_url = current_url+'posts/';
        $.ajax({
             type: "GET",
             url: dest_url,
             // data: {username:$("#username").val(), content:$("#content").val()},
             dataType: "json",
             success: function(data){

                 // alert(data['list'].length)
                 var len = data['list'].length
                 // alert(len)
                 $('#data_div').empty();   //清空resText里面的所有内容

                 var tableStr = "<table class='tab-list' width='99%'>";

                 tableStr = tableStr
                   + "<tr class='list-header'>"
                   +"<td width='5%' ><b>ID</b></td>"
                   +"<td width='20%'><b>SneakerName</b></td>"
                   +"<td width='10%'><b>ReleaseDate</b></td>"
                   +"<td width='10%'><b>PublishDate</b></td>"
                   +"<td width='60%'><b>SneakerDescription</b></td>"
                   +"<td width='5%'></td>"
                   +"<td width='5%'></td>"
                   +"</tr>";

                 for(var i = 0; i < len; i++){
                     // alert(i)
                     // alert(data['list'][i].pk)
                     var pknum = data['list'][i].pk;
                     var d_pknum = -pknum
                     // alert(pknum.toString(10))
                     // var spknum = pknum.toString(10);
                     tableStr = tableStr + "<tr>"
                         + "<td>" + data['list'][i].pk + "</td>"
                         + "<td>" + data['list'][i].fields.title + "</td>"
                         + "<td>" + data['list'][i].fields.sneakerReleaseDate + "</td>"
                         + "<td>" + data['list'][i].fields.sneakerPublishDate + "</td>"
                         // + "<td>" + data['list'][i].fields.sneakerDescription + "</td>"
                         + "<td>" + data['list'][i].fields.body + "</td>"
                         + "<td width='10%'><button id= "+pknum+"  style='width: 60px' class='edit_btn' value= >Edit</button></td>"
                         + "<td width='10%'><button id= "+d_pknum+" style='width: 60px' class='del_btn'>Delete</button></td>"
                         + "</tr>";
                 }

                 tableStr = tableStr + "</table>";
                 //添加到div中
                 $("#data_div").html(tableStr);
                 },
         });

    });

//--------------------------------------------------

    $("#post_button").click(function () {
        window.location.href="/sneakers/new";
    })

    $(document).on("click", ".edit_btn", function() {
        var id = this.id
        // alert( id )
        // alert( $(this).attr("value") )
        window.location.href="/sneakers/editsneaker/?id="+id;
    });

    $(document).on("click", ".del_btn", function() {
        var id = this.id
        id = -id;
        // window.location.href="/sneakers/management";
        dest_url = current_url+'delete/?id='+id;
        $.ajax({
             type: "GET",
             url: dest_url,
             // data: {username:$("#username").val(), content:$("#content").val()},
             dataType: "json",
             success: function(data){
                 // alert(data['list'].length)
                 var len = data['list'].length
                 // alert(len)
                 $('#data_div').empty();   //清空resText里面的所有内容

                 var tableStr = "<table class='tab-list' width='99%'>";

                 tableStr = tableStr
                   + "<tr class='list-header'>"
                   +"<td width='5%' ><b>ID</b></td>"
                   +"<td width='20%'><b>SneakerName</b></td>"
                   +"<td width='10%'><b>ReleaseDate</b></td>"
                   +"<td width='10%'><b>PublishDate</b></td>"
                   +"<td width='60%'><b>SneakerDescription</b></td>"
                   +"<td width='5%'></td>"
                   +"<td width='5%'></td>"
                   +"</tr>";

                 for(var i = 0; i < len; i++){
                     // alert(i)
                     // alert(data['list'][i].pk)
                     var pknum = data['list'][i].pk;
                     var d_pknum = -pknum
                     // alert(pknum.toString(10))
                     // var spknum = pknum.toString(10);
                     tableStr = tableStr + "<tr>"
                         + "<td>" + data['list'][i].pk + "</td>"
                         + "<td>" + data['list'][i].fields.title + "</td>"
                         + "<td>" + data['list'][i].fields.sneakerReleaseDate + "</td>"
                         + "<td>" + data['list'][i].fields.sneakerPublishDate + "</td>"
                         // + "<td>" + data['list'][i].fields.sneakerDescription + "</td>"
                         + "<td>" + data['list'][i].fields.body + "</td>"
                         + "<td width='10%'><button id= "+pknum+"  style='width: 60px' class='edit_btn' value= >Edit</button></td>"
                         + "<td width='10%'><button id= "+d_pknum+" style='width: 60px' class='del_btn'>Delete</button></td>"
                         + "</tr>";
                 }

                 tableStr = tableStr + "</table>";
                 //添加到div中
                 $("#data_div").html(tableStr);
             }

         });


    });


});








