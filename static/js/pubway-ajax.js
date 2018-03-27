$('#likes').click(function(){
    var plcid;
    plcid = $(this).attr("data-plcid");
    $.get('/pubway/like/', {place_id: plcid}, function(data){
        $('#like_count').html(data);
            $('#likes').hide();
    });
});