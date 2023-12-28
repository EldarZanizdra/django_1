function test(){
    $('#btn').click(function(){
        $.ajax('/test/', {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'text': $('#text').val()
            },
            'success': function(data){
                document.getElementById('resp').innerHTML = data['resp']
            }
        })
    })
}

