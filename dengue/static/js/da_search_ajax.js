$(function(){

    $('#dasearch').keyup(function() {
    
        $.ajax({
            type: "GET",
            url: "/dasearch/",
            data: { 
                'dasearch_text' : $('#dasearch').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
        
    });

});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#dasearch-results').html(data);
}


