$(document).ready(function(){

    $('body').on('click', 'input[type=checkbox]', function (){
        var trigger = $(this).attr("id");
        var target = trigger.replace("checkbox-","table-");
        $("#"+target).toggle();
    });

    var css_dirty = $("#css pre").html()
    var css_json = CSSJSON.toJSON(css_dirty);
    var css_clean = CSSJSON.toCSS(css_json);
    $("#css pre").html(css_clean)

})