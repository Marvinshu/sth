$('button[type="button"]').click ->
    pwd = $('input[name="pwd"]').val()
    new_pwd = $('input[name="new_pwd"]').val()
    re_pwd = $('input[name="re_pwd"]').val()

    data = {
        pwd: pwd
        new_pwd: new_pwd
        re_pwd: re_pwd
    }

    $.only_ajax({
        url: "/j/user/reset_pwd",
        data: data
        success: (r)->
            if r.result
                $('input[name="pwd"]').val('')
                $('input[name="new_pwd"]').val('')
                $('input[name="re_pwd"]').val('')
                $.tip(r.msg)
            else
                $.alert(r.msg)
    })
