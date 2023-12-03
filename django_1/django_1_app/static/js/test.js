function test(){
    $('#btn').click(function(){
        $.ajax('/test/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            }
        })
    })
}

$(document).ready(function(){
    test();
})