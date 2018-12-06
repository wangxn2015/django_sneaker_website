

$(document).ready(function(){

    $(".number li").click(function () {
        $(this).addClass("current_pic").siblings().removeClass("current_pic");
        var index = $(this).index();
        $(".img li").eq(index).fadeIn(800).siblings().fadeOut(800);
        $(".date li").eq(index).show().siblings().hide();
        
    });
    

    var i = 0;
    $(".img li").eq(i).stop().show().siblings().hide();
    $(".date li").eq(i).show().siblings().hide();
    var tim = setInterval(move,3500);

    function move() {
        $(".number li").eq(i).addClass("current_pic").siblings().removeClass("current_pic");
        $(".img li").eq(i).stop().fadeIn(800).siblings().stop().fadeOut(800);
        $(".date li").eq(i).show().siblings().hide();

        i++;
        if(i>2)i=0;
    }

    $(".pic_area").hover(function () {
        clearInterval(tim);
    },function () {
        tim = setInterval(move,3500);
    })

    // $("h3").click(function(){
    //     $(this).hide();
    // });
    // $("h1").click(function(){
    //     $(this).hide();
    // });


})