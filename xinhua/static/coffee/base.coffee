$.extend({
    app: angular.module('app', ['ngRoute'])

    tip: (msg)->
        $('#msg').attr('class', 'alert alert-info')
        $('#msg').css('display', 'block')
        $('#msg').html(msg)

    alert: (msg)->
        $('#msg').attr('class', 'alert alert-danger')
        $('#msg').css('display', 'block')
        $('#msg').html(msg)

    only_ajax: (option)->
        $.ajax({
            method: option.method,
            url: option.url,
            data: option.data,
            type: option.type or 'POST'
            success: (r)->
                option.success(r)

            fail: ->
                foption.ail()
        })
})
