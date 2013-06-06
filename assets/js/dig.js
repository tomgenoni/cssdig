$(document).ready(function(){

    $('input[type=checkbox]').click(function(){
        var trigger = $(this).attr("id");
        var target = trigger.replace("checkbox-","table-");
        $("#"+target).toggle();
        report_top = $("#report").scrollTop();
        target_top = $("#"+target).offset().top;
        if ( $(this).attr("checked") == "checked") {
            $('#report').animate({
                 scrollTop: target_top + report_top - 25
            }, 500);
        }
    });

    var css_dirty = $("#css pre").html()
    var css_json = CSSJSON.toJSON(css_dirty);
    var css_clean = CSSJSON.toCSS(css_json);
    $("#css pre").html(css_clean)

})