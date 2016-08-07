$('#btn-login').click ->
    username = $("input[name='username']").val()
    password = $("input[name='password']").val()
    $.only_ajax({
        url: "/j/login",
        data: {username: username, password: password}
        success: (r)->
            if r.login
                window.location.href = '/'
            else
                $.alert r.msg
    })
