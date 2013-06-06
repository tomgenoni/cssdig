$(document).ready(function(){

    $('body').on('click', 'input[type=checkbox]', function (){
        var trigger = $(this).attr("id");
        var target = trigger.replace("checkbox-","table-");
        $("#"+target).toggle();
    });

})