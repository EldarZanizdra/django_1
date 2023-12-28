$(function(){
    $('#btt').click(function(){
        var button = $(this)
        $.ajax(button.data('url'), {
            'type': 'POST',
            'dataType': 'json',
            'async': true,
            'data': {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'name': $('#name').val(),
                'status': $('#status').val(),
                'deadline': $('#deadline').val(),
                'priority': $('#priority').val(),
            },
            'success': function(data){
                document.getElementById('tasks').innerHTML += data
            }
        })
    })
})


$(document).ready(function(){
    test();
})